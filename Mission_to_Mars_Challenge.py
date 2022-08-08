#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install webdriver_manager


# In[2]:


#!pip install splinter


# In[3]:


#!pip install beautifulsoup4


# In[4]:


#!pip install bs4


# In[1]:


from bs4 import BeautifulSoup


# In[2]:


# Import Splinter and BeatifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# Set the executable path in the next cell, then set up the URL (NASA Mars News) fro scraping

# In[7]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# We will assign the url and instruct the browser to vist it

# In[8]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[9]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')  #looking for the <div />
#This elemt will holds all of the other elements within it
# (.) is to select classes


# #### open the MARS Planet Science

# In[10]:


# starting the scraping, searching for the title
slide_elem.find('div', class_='content_title')


# In[11]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

#Once executed. the result is the most recent title published on the website. When the website is updated and 
#a new article is posted, when our code Is run again, It will return that article instead


# There are two methods used to find tags and attributes with Beautifu Soup:
# 
# • .find() is used When we want onlv the first class and attribute we've specified.
# 
# • .find_all() is used when we want to retrieve all of the tags and attributes

# In[12]:


# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # 10.3.4

# ### Featured Images

# In[13]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[14]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


#hemisphere_image_urls


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

### to download photos from Mars Facts web page


# In[ ]:


# This is the url of the web page: https://mars.nasa.gov/all-about-mars/facts/
#df = pd.read_html('https://galaxyfacts-mmars.com')[0]
df = pd.read_htmldf = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


# To ennd the automated browsing session.
# Otherwise will continue for listening instructions
browser.quit()


# ----------------------------------------

# # Challenge

# In[ ]:


# Set the executable path and initialize Splinter
# Step 1
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://marshemispheres.com/'
browser.visit(url)

# Optional delay for loading the page
#browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Step 2
hemisphere_image_urls = []


# In[ ]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

urls = browser.find_by_css('a.product-item img')

for i in range(len(urls)):
    hemisphere = {}
    browser.find_by_css('a.product-item img')[i].click()
    
    sample_elem = browser.urls.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css('h2.title').text
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()    


# In[ ]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()


# # End

# In[ ]:




