from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

path = "chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

b = list()
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name = a.find('div', attrs = {'class':'_4rR01T'})
    b.append(name.text.split('-')[0])
print(b)

df = pd.DataFrame({'laptop Names' : b})
df.to_csv('laptop names test', index=True, encoding= 'utf8') 