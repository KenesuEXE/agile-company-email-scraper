from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time

url = "https://scaledagile.com/business-solutions/find-a-partner/#id=0010W00002cIOTSQA4"

# Load website
options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Scrape info
company = soup.find("h1", class_="summary-title").text
email = soup.find("lightning-formatted-email").text
phone = soup.find("lightning-formatted-phone").text

print(company, email, phone)