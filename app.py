# We'll use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for

# We'll use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
import mongodf

# to use the scraping code, we will convert from Jupyter notebook to Python
import scraping

app = Flask(__name__)

# use flask_pymongo to set up mongo connection
# tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app-> Is the URI we'll be using to connect our app to Mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page.
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

    if __name__ == "__main__":
        app.run()
        
  
