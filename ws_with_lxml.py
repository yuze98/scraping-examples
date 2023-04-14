import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content,'lxml')

box = soup.find('article', class_='main-article')
movie_name = box.find('h1').text

transcript = box.find('div',class_ = 'full-script').get_text(strip=True, separator=' ')

with open(f'{movie_name}.txt','w') as file:
    file.write(transcript)
print(movie_name)