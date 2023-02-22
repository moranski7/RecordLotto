import requests
from selenium import webdriver

response = requests.get("https://www.google.com/")
print (response.status_code)
print ()


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
driver.get("https://www.olg.ca/en/lottery/winning-numbers-results.html")
html = driver.page_source
with open("olgWinningPage.txt", "w", encoding="utf-8") as file:
	file.write(html)
	file.close()
driver.quit()

