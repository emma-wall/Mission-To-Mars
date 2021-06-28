# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# JPL Space Images Freatured Image
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()

# D1: Scrape High-Resolution Mars' Hemisphere Images and Titles
# Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#hem_links = browser.links.find_by_partial_text('Hemisphere Enhanced')
hem_links = browser.find_by_css("a.product-item img")

# create for loop, itereate through the tags 
#for link in hem_links
for i in range(len(hem_links)):
    # a) create an empty dictiornay 
    hemispheres = {}
    
    # b) click on hemisphere link
    #link.click()
    #hem_links[i].click()
    browser.find_by_css("a.product-item img")[i].click()
    # c) navigate to full resolution and retrieve URL string and title for the hemisphere image
    html = browser.html
    hem_soup = soup(html, 'html.parser')

    img_path = hem_soup.find('div', id="wide-image")
    img_url_rel = img_path.find('a', target='_blank').get('href')
    img_url = url+img_url_rel
    img_title = hem_soup.find('h2', class_='title').text

    #save image URL and title to hemisphere dictionary
    hemispheres['img_url'] = img_url
    hemispheres['title'] = img_title
    #add hemisphere dictionary to hemisphere_image_urls list
    hemisphere_image_urls.append(hemispheres)
    # d) navigate back to the beginning to get next hemisphere image
    browser.back()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
