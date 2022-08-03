# Image-Matching-Python-Script

# First I have install Selenium in Ubuntu-
- sudo install selenium

# Then I have installed BeautifulSoup-
- sudo apt-get install python3-bs4

# Then I have followed a document for installing the webdriver-
- The link of the documentation,
      https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

# Image Matching steps-
- First, I have used the web driver to achieve the search url. 
- Then, took another variable for the keyword or the search tags. 
- Afterthat, I have used BeautifulSoup for parsing and scraping the HTML page.
- And I have also created the image tag list using which I have created other two lists of
  image urls and image alt (alternate text of an area).
- Then, using for loops, the iteration took place of finding the keyword in the alt of the 
  images. And the matched alt of an image is appended in a list name match_keyword.
