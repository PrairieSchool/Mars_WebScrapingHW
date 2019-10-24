    # To add a new cell, type '#%%'
    # To add a new markdown cell, type '#%% [markdown]'
    #%% [markdown]
    # <h2>Read Headline & Teaser with BeautifulSoup</h2>
def scrape():
    #%%
    from bs4 import BeautifulSoup
    import requests


    #%%
    #using 'requests' to get news from nasa url, translating to html
    news_url = "https://mars.nasa.gov/news/"
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text,"html.parser")

    #finding "Features" on nasa website, iterating through to save first headline and teaser paragraph
    Features = soup.find_all("div",class_="features")
    for feature in Features:

        headTitle = feature.find("div",attrs={"class":"content_title"})
        head = headTitle.find("a",href=True).text.strip("\n")
        teaser = feature.find("div",attrs={"class":"rollover_description_inner"}).text.strip("\n")

    #    print('-----------------')
    #    print(head)
    #    print(teaser)

    #%% [markdown]
    # <h2>Save Image with BeautifulSoup and Splinter</h2>

    #%%
    from splinter import Browser
    from bs4 import BeautifulSoup

    # opening Chrome browser, visiting nasa url
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #translating web page into html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #finding featured image and concatinating url with endpoint to save url for featured image
    marsPic3 = soup.find("article",class_="carousel_item")
    link = marsPic3.a['data-fancybox-href']
    featured_image_url = (f"https://www.jpl.nasa.gov{link}")
    browser.visit(featured_image_url)
    #print(featured_image_url)

    #%% [markdown]
    # <h2>Mars Weather scraped from twitter</h2>

    #%%
    from splinter import Browser
    from bs4 import BeautifulSoup

    #opening chrome browser and visiting mars's twitter feed
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)


    #%%
    #translating twitter page into html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #parsing html to save most recent weather report
    mars_weather = soup.find("div", id="timeline").    find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    #mars_weather

    #%% [markdown]
    # <h2>Using Pandas to read table on Space Facts website</h2>

    #%%
    #using pandas to read one of the tables on website and saving as a dataframe
    import pandas
    mars_facts_scrape = pandas.read_html("https://space-facts.com/mars/")
    mars_facts_df = mars_facts_scrape[1]
    #print(mars_facts_df)


    #%%
    #converting dataframe to html table
    mars_facts = mars_facts_df.to_html()
    #print(mars_facts)

    #%% [markdown]
    # <h2>Mars Hemispheres</h2>

    #%%
    from splinter import Browser
    from bs4 import BeautifulSoup

    #using BeautifulSoup and Splinter to open Chrome browser and navigate to Astrogeology web page
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    #translating webpage into html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #%%
    #using splinter to iterate through page and click on first four links that contain the word "Enhanced"
    #saving the title and endpoint of each picture as dictionary
    #appending a list of dictionaries

    Hemispheres = []
    HemispheresAlt = []

    for i in range(4):

        browser.click_link_by_partial_text("Enhanced")
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemi_title = soup.find("div",class_="container").find("h2",class_="title").text
        hemi_image = soup.find("a",target="_blank")["href"]
        image_url = (f"https://astrogeology.usgs.gov{hemi_image}")

        hemiDict = {f"hemiTitle{i}": hemi_title, f"hemiImage{i}": hemi_image}
        hemiDictAlt = {"hemiTitle":hemi_title,"hemiImage":hemi_image}

        Hemispheres.append(hemiDict)
        HemispheresAlt.append(hemiDictAlt)


    #%%
    #list of title/image numbered dictionaries 
    #print(Hemispheres)


    #%%
    #list of title/image non-numbered dictionaries. Not sure which will be ultimately used  
    #print(HemispheresAlt)


    #%%
    MarsMasterDictionary = {
            "Head":head,
            "Teaser":teaser,
            "Feat":featured_image_url,
            "Weather":mars_weather,
            "Facts":mars_facts,
            "HemiImages":HemispheresAlt
        }

    return MarsMasterDictionary
    #print(MarsMasterDictionary)
    #%%


