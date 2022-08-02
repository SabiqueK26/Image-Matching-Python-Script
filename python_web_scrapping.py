from selenium import webdriver
import bs4
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/home/asus/chromedriver")
search_url = "https://www.freepik.com/search?format=search&query=car"
driver.get(search_url)

key_word = "car"

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

divTag = soup.select('section.showcase.mg-none-i.showcase--spr div.row figure.showcase__item.caption div.showcase__content a.showcase__link')
# print(len(divTag))
# print(divTag)
imgTag = []
for x in divTag:
    imgTag.append(x.find('img'))
# print(len(imgTag))
# print(imgTag)

images_url = [{img['src']} for img in imgTag]
# print(images_url)

list_of_alt = [alt['alt'] for alt in imgTag]
print(list_of_alt)

# for i in range(len(list_of_alt)):