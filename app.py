from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsTheRedDatabase")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    Mars_Mongo_Data = mongo.db.Mars_Mongo_Data.find_one()

    # Return template and data
    return render_template("index.html", Mars_Mongo_Data=Mars_Mongo_Data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    # Run the scrape function
    Mars_Mongo_Data = mongo.db.Mars_Mongo_Data
    MarsMasterDictionary = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    Mars_Mongo_Data.update({}, MarsMasterDictionary, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

