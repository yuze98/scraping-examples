import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'

result = requests.get(website)

content = result.text
soup = BeautifulSoup(content,'lxml')

box = soup.find_all('a',href=True)

links = [link['href'] for link in box]

filtered_links = []
for link in links:
    if('movie/' in link):
        filtered_links.append(link)

# print(links)

def movie_scrap(s):
    b = s.find('article', class_='main-article')
    movie_name = b.find('h1').text
    transcript = b.find('div', 'full-script').get_text(strip=True,separator=' ')
    
    return movie_name, transcript

for link in filtered_links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content,'lxml')
    mov,tr = movie_scrap(soup)
    with open(f'movie_scrap/{mov}.txt','w') as file:
        file.write(tr)

