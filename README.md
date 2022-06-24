# 12 Web Scraping - Mission to Mars

## Background

A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Skills

jupyter notebook | BeautifulSoup | pandas | Requests/Splinter | Pymongo | boostrap

### Web Scraping

The Jupyter Notebook file called `mission_to_mars.ipynb` contains the scraping code used.

#### NASA Mars News

* Scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) and collects the latest News Title and Paragraph Text.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

#### JPL Mars Space Images - Featured Image

* Visits the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
* Uses splinter to navigate the site and finds the image url for the current Featured Mars Image.

```python
# Example:
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/images/largesize/PIA16225_hires.jpg'
```

#### Mars Facts

* Visits the Mars Facts webpage [here](https://space-facts.com/mars/) and scrapes the table containing facts about the planet including Diameter, Mass, etc.

#### Mars Hemispheres

* Visits the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and obtains high resolution images for each of Mar's hemispheres.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

### MongoDB and Flask Application

MongoDB and Flask are used to create a new HTML page that displays all of the information that was scraped before.

* The jupyter notebook was converted into a Python script called `scrape_mars.py` where the function `scrape` executes all the scraping code and returns one Python dictionary containing all of the scraped data.
* A route called `/scrape` imports the `scrape_mars.py` script and calls the `scrape` function.
* The return value is stored in Mongo as a Python dictionary.
* The root route `/` queries the Mongo database and passes the mars data into an HTML template to display the data.
* The template HTML file called `index.html` takes the mars data dictionary and displays all of the data in the appropriate HTML elements.

<img width="569" alt="Screen Shot 2021-05-04 at 6 12 13 pm" src="https://user-images.githubusercontent.com/77761497/175207254-71994efc-301a-4343-9fd5-e404ebde367a.png">
<img width="591" alt="Screen Shot 2021-05-04 at 6 12 29 pm" src="https://user-images.githubusercontent.com/77761497/175207274-84092789-23f1-4b85-a07f-5878deebffca.png">

