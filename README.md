# Image-Matching-Python-Script

# First I have install Selenium in Ubuntu-
- sudo install selenium

# Then I have installed BeautifulSoup-
- sudo apt-get install python3-bs4

# Then I have followed a document for installing the webdriver-
- The link of the documentation,
      https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

# Image Matching steps-
- First, I have used the **Selenium** for importing web driver to achieve the search url. 
- Then, took another variable for the **'key_word'** i.e. the search tag. 
- Afterthat, I have used **BeautifulSoup** for parsing and scraping the HTML page.
- And I have also created the image tag list named **'imgTag'** using which I have 
  created other two lists of **image urls** i.e. the data source and **image alt** 
  (alternate text of an area).
- Then, using for loops, the iteration took place of finding the **'key_word'** in the 
  alt of the images. And the matched alt of an image is appended in a list name 
  **'match_keyword'**.
- I have created a dictionary where I zipped the two lists which are the **'list_of_alt'** 
  as key and **'images_url'** as values. 
- And an empty dictionary was created named **'match_image'** for the matched search tags 
  and it's url.
- By using for loop and if statements, I have updated the empty list with the 'image alt' 
  as key which matches with the **'key_word'** and it's corresponding **'url'** or 
  **'data-src'** as value.
- Finally, I have printed the dictionary **'match_image'**.