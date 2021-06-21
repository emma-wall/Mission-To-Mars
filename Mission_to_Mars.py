# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Visit the NASA website to scrape
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

#Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

#Use parent element to find the fist tage and save it as news_title
news_title = slide_elem.find('div', class_='content_title').get_text()
print(news_title)

#Use the parent element to find the paragraph text
news_summary = slide_elem.find('div', class_='article_teaser_body').get_text()
print(news_summary)

# ## Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

#Find the relative image url
img_url_rel = img_soup.find('img', class_='thumbimg').get('src')
print(img_url_rel)

# ## Mars Facts
facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
facts_df.columns=['description', 'Mars', 'Earth']
facts_df.set_index('description', inplace=True)
facts_df

facts_df.to_html()

browser.quit()
