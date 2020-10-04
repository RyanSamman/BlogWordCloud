import json
from time import sleep
from selenium import webdriver

# Start driver
driver = webdriver.Chrome()

# Go to website
driver.get("https://lms.kau.edu.sa")
# Then, Manually Login, and move to the weekly writing page

def openList():
    # Open Menu 
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div/div[3]/div/div[2]/div[4]/div/button").click()

def getBlogs():
    # Get List Element containing all the blog links
    blogList = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div/div[3]/div/div[2]/div[4]/div/ul")

    # Retrieve children of <ul> element
    return blogList.find_elements_by_class_name("user")

def getLinks(blgs):
    # Retrieve anchor links in every list element
    return [e.find_element_by_tag_name("a").get_property("href") for e in blgs]

def loadPageAndScrapeBlog(url):
    sleep(2) # Sleep while the previous page loads
    driver.get(url) # Redirect to blog URL
    e = driver.find_elements_by_class_name("entryText") # Select the element containing the blog text
    return e[0].text # Obtain the raw text from the latest blog element

def saveData(data):
    with open("rawBlogText.json", 'w') as f:
        json.dump(data, f, indent=2)


'''
Run in the Interactive Shell

python scraper.py -i

Open blogs menu


# Get all blog links
blogs = getBlogs()
blogLinks = getLinks(blogs)

# Get all blog text
blogTexts = [loadPageAndScrapeBlog(url) for url in blogLinks]

# Save the blog data
saveData(blogTexts)
'''