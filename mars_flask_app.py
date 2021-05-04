# Step 2 - MongoDB and Flask Application
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. 
# 2- Create a route called /scrape that will import your scrape_mars.py script and call your scrape function. Store the return value in Mongo as a Python dictionary.

# 3- Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

# 4- Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()
    # Render an index.html template and pass it the data retrieved from the db
    return render_template("index.html", mars=mars_dict)


@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
