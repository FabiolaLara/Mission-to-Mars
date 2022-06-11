
from bs4 import BeautifulSoup


# Import Splinter and BeatifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# Set the executable path in the next cell, then set up the URL (NASA Mars News) fro scraping

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')  #looking for the <div />
#This elemt will holds all of the other elements within it (.) is to select classes
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'

news_title = slide_element.find('div', class_='content_title').get_text()
news_title

# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p




