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
# print(list_of_alt)

match_keyword = []
for i in range(len(list_of_alt)):
    str = ''.join(list_of_alt[i])
    # print(str)
    words = str.split(" ")
    # print(words)
    for j in range(len(words)):
        if words[j] == key_word:
            sentence = ' '.join(words)
            print(sentence)
            match_keyword.append(sentence)
            break
        else:
            continue
print(match_keyword)
print(list_of_alt)

for alt in range(len(match_keyword)):
    if match_keyword[alt] in list_of_alt:
        print("Done")