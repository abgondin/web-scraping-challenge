# Step 2 - MongoDB and Flask Application
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. 
# 1- Convert your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}


    # Mars News URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the latest news title
    latest_article = soup.find_all('div', class_='list_text')[0]
    news_title = latest_article.find('div', class_='content_title').text
    # Retrieve the latest news paragraph
    news_p = latest_article.find('div', class_='article_teaser_body').text


    # Mars Image to be scraped
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    jpl_index_url = f'{jpl_url}index.html'
    browser.visit(jpl_index_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Assign the featured image url to a variable
    relative_image_path = soup.find('img', class_ = "headerimage")["src"]
    featured_image_url = jpl_url + relative_image_path

    
    # Mars facts to be scraped, converted into html table
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    # Store the first table into a df, containing the information about mars
    mars_facts_df = tables[0]
    mars_facts_df.columns = ["Description", "Mars"]
    mars_facts_df = mars_facts_df.set_index("Description")
    # Using pandas to convert df to html
    mars_html_table = mars_facts_df.to_html()
    
    # Mars hemisphere name and image to be scraped
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain Mars hemispheres info
    hemispheres = soup.find_all('div', class_='item')
    # Set an empty list to contain all the dictionary info 
    hemispheres_info = []

    # Iterate through each hemisphere
    for item in hemispheres:
        # Extract title using bs find method
        title = item.find('div',class_='description').h3.text
        # Extract image link by browsing to hemisphere page
        item_href = item.a["href"]    
        browser.visit('https://astrogeology.usgs.gov' + item_href)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find('div', class_='downloads')
        img_href = img.a['href']
        img_url = img_href

        # Create Dictionary to store title and url info
        hemi_dict = {}
        hemi_dict['title'] = title
        hemi_dict['img_url'] = img_url
        hemispheres_info.append(hemi_dict)

    # Create a mars_data_dic to store all the information to be displayed in the app

    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(mars_html_table),
        "hemisphere_images": hemispheres_info
        }
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_dict