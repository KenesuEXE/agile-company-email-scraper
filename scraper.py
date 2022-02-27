import requests
from bs4 import BeautifulSoup

url = "https://scaledagile.force.com/aura?r=1&aura.ApexAction.execute=1"
response = requests.get(url)
data = response.json()
soup = BeautifulSoup(data["results"], "lmxl")
print(soup.prettify())


"""from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.get("https://quotes.toscrape.com/js")

soup = BeautifulSoup(driver.page_source, "lxml")
authors = soup.find_all("small", class_="author")
for author in authors:
    print(author)

driver.quit()"""
"""
from helium import *
from bs4 import BeautifulSoup



url = "https://quotes.toscrape.com/"
browser = start_chrome(url, headless=True)
soup = BeautifulSoup(browser.page_source, "html.parser")

print(soup.prettify())
"""




# Works but only returns page logo
# I need to find a way to let the website load the calendar first before retrieving the HTML
"""
url = "https://scaledagile.com/calendar/?course_id=SAFe+Scrum+Master"

browser = start_chrome(url, headless=True)


soup = BeautifulSoup(browser.page_source, "html.parser")
companies = soup.find_all("img")
for company in companies:
    print(company)
"""