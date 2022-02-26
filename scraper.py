from helium import *
from bs4 import BeautifulSoup

url = "https://scaledagile.com/calendar/?course_id=SAFe+Scrum+Master"

browser = start_chrome(url, headless=True)

# Works but only returns page logo
# I need to find a way to let the website load the calendar first before retrieving the HTML

soup = BeautifulSoup(browser.page_source, "html.parser")
companies = soup.find_all("img")
for company in companies:
    print(company)