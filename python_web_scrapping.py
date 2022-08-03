from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/home/asus/chromedriver")
search_url = "https://www.freepik.com/search?format=search&query=car"
driver.get(search_url)

key_word = "car"

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
divTag = soup.select('section.showcase.mg-none-i.showcase--spr div.row figure.showcase__item.caption div.showcase__content a.showcase__link')

imgTag = []
for x in divTag:
    imgTag.append(x.find('img'))

images_url = [{img['data-src']} for img in imgTag]
list_of_alt = [alt['alt'] for alt in imgTag]

match_keyword = []
for i in range(len(list_of_alt)):
    str = ''.join(list_of_alt[i])
    words = str.split(" ")
    for j in range(len(words)):
        if words[j] == key_word:
            sentence = ' '.join(words)
            match_keyword.append(sentence)
            break
        else:
            continue

dictionary = dict(zip(list_of_alt, images_url))
match_image = {}
for key, value in dictionary.items():
    if key in match_keyword:
        match_image.update({key: value})
print(match_image)