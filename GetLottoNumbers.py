import sys

def isConnected():
	import requests
	test_connection = requests.get("https://www.google.com/")
	return test_connection.status_code == 200

def getLottoWinningPage():
	from selenium import webdriver
	if isConnected():
		op = webdriver.ChromeOptions()
		op.add_argument('headless')
		driver = webdriver.Chrome(options=op)
		driver.get("https://www.olg.ca/en/lottery/winning-numbers-results.html")
		html = driver.page_source
		driver.quit()
		return html
	else:
		return None

def getLottoNumbers(html):
	import re
	numberPatterns = r"<div class=\"lotto-ball-large selected lotto-ball\"><div class=\"ball-number\">(\d\d)"
	lottoMaxPattern = r"alt=\"LOTTO MAX\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
	lotto649Pattern = r"alt=\"LOTTO 6/49\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
	lottoMaxContents = ""
	lotto649Contents = ""
	parseResult = None
	lottoMaxNumbers = None
	lotto649Numbers = None

	parseResult = re.search(lottoMaxPattern, html)
	if parseResult:
		lottoMaxNumbers = re.findall(numberPatterns, parseResult.group(0))
	
	parseResult = re.search(lotto649Pattern, html)
	if parseResult:
		lotto649Numbers = re.findall(numberPatterns, parseResult.group(0))

	return lottoMaxNumbers, lotto649Numbers

def writeToCsvFile(fileName, lottoNumbers):
	import csv
	import os
	from datetime import datetime
	fileExist = os.path.isfile(fileName)
	if fileExist:
		with open(fileName, "a+") as csvfile:
			fieldnames = ["Number", "Date(YYYY-MM-DD)"]
			w = csv.DictWriter(csvfile, fieldnames=fieldnames)
			numbers = ",".join(lottoNumbers)
			w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
			csvfile.close()
	else:
		with open(fileName, "w+") as csvfile:
			fieldnames = ["Number", "Date(YYYY-MM-DD)"]
			w = csv.DictWriter(csvfile, fieldnames=fieldnames)
			w.writeheader()
			numbers = ",".join(lottoNumbers)
			w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
			csvfile.close()
	return


def recordLottoNumbers():
	#Check file for Today's date to avoid double recording
	html = getLottoWinningPage()

	if html:
		lottoMaxNumbers,lotto649Numbers = getLottoNumbers(html)
		writeToCsvFile(r"Lotto_Max_Numbers.csv", lottoMaxNumbers)
		writeToCsvFile(r"Lotto_649_Numbers.csv", lotto649Numbers)
	else:
		print("TBA")
		sys.exit(1)

def main():
	recordLottoNumbers()
	sys.exit(0)

main()