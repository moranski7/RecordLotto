import sys
import os
import csv
from datetime import datetime

def fileExistCheck(fileName):
	"""Check to see if a file exist. True if yes. False otherwise."""
	return os.path.isfile(fileName)

def restoreTotal (fileMax, file649):
	"""Creates a text file for collecting the total times numbers in a lotto has appeared. If csv files exist, tallies the total
	for that lotto. Writes to new file."""
	totalMax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	total649 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	#If csv record for lotto Max exist, read the file and tallies the numbers.
	if fileExistCheck(fileMax):
		with open(fileMax, "r") as csvfile:
			r = csv.DictReader(csvfile)
			for row in r:
				for x in row["Number"].split(","):
					totalMax[int(x)] += 1
			csvfile.close()

	#If csv record for lotto 649 exist, read the file and tallies the numbers.
	if fileExistCheck(file649):
		with open(file649, "r") as csvfile:
			r = csv.DictReader(csvfile)
			for row in r:
				for x in row["Number"].split(","):
					total649[int(x)] += 1
			csvfile.close()

	#Record new total to text file.
	with open("tracked_Numbers.txt", "w") as file:
		stringMax = ",".join([str(x) for x in totalMax])
		string649 = ",".join(str(x) for x in total649)
		file.write(stringMax)
		file.write("\n")
		file.write(string649)
		file.close()
	return

def areNumbersRecorded(fileName):
	"""Check to see if numbers have been recorded. Checks for today's date in csv file. Returns True if yes. False otherwise."""
	today = datetime.today().strftime('%Y-%m-%d')
	with open(fileName, "r") as csvfile:
		csvReader = csv.DictReader(csvfile)
		for row in csvReader:
			if today in row.values():
				return True
		csvfile.close()
	return False

def numbersOut():
	"""Numbers for Lotto Max, Lotto 649 are both out Sunday and Thursday in the morning.
	Returns True if today's date is Sunday or Thursday past 9 am."""
	dt = datetime.now()
	day = dt.strftime('%A')
	hour = dt.hour
	return (day == "Sunday" or day == "Thursday") and (hour > 9)

def isConnected():
	"""Checks for an internet connection. Returns true if connects to Google. False otherwise."""
	import requests
	test_connection = requests.get("https://www.google.com/")
	requests.session().close()
	return test_connection.status_code == 200

def getLottoWinningPage():
	"""Get the webpage from Olg. Olg uses javascript to populate it's webpage content. Request module only gets the html content.
	Therefore uses webdriver from selenium module to access the javascript content.
	Returns a string that contains the webpage content on success. Returns None if failed.

	Note: Uses Chrome browser as using the FireFox browser method causes any open FireFox browser to freeze."""
	from selenium import webdriver
	if isConnected():
		op = webdriver.ChromeOptions()
		op.add_argument('headless') #Prevents a browser from opening up.
		driver = webdriver.Chrome(options=op) 
		driver.get("https://www.olg.ca/en/lottery/winning-numbers-results.html")
		html = driver.page_source
		driver.quit()
		return html
	else:
		return None

def getLottoNumbers(html):
	"""Gets the letto numbers from the page source.

	Uses Regex to parse the page. Regex is applied in the following manner:
		1. Get the section containing the numbers. This should contain only one result.
		2. Get the individual numbers from the results of step 1. This should result in a list of strings representing numbers.

	Returns: On success returns a tuple containing two list of strings. On failure, tuple contains None."""
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
	"""Writes the results to file. If file exist, appends to the end of the file. Otherwise makes a 
	new file."""
	fileExist = fileExistCheck(fileName)
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

def recordTotal(lottoMaxNumbers, lotto649Numbers):
	"""Opens the tracked_Numbers.txt file and tally the new number lotto numbers into the result.
	If params are None, nothing happens.

	Note: Function assumes that tracked_Numbers.txt file exists."""
	with open("tracked_Numbers.txt", "r") as file:
		stringMax = file.readline()
		string649 = file.readline()
		file.close()
	numbersMax = [int(x) for x in stringMax.strip().split(",")]
	numbers649 = [int(x) for x in string649.strip().split(",")]

	if lottoMaxNumbers:
		for x in lottoMaxNumbers:
			numbersMax[int(x)] += 1
	if lotto649Numbers:
		for x in lotto649Numbers:
			numbers649[int(x)] += 1
	newNumMax = ",".join(str(x) for x in numbersMax)
	newNum649 = ",".join(str(x) for x in numbers649)

	with open("tracked_numbers.txt", "w") as file:
		file.write(newNumMax)
		file.write("\n")
		file.write(newNum649)
		file.close()
	return


def recordLottoNumbers():
	"""Gets the current winning olg numbers for Lotto Max and Lotto 649 and records them in separate csv files.
	Tallies the total number of times a lotto number has appeared and record in a text file."""
	html = None
	LottoMaxFile = r"Lotto_Max_Numbers.csv"
	Lotto649File = r"Lotto_649_Numbers.csv"
	trackFile = r"tracked_numbers.txt"

	if not fileExistCheck(trackFile):
		restoreTotal (LottoMaxFile, Lotto649File) #Goes through csv files and retallies the lotto numbers.
	if not fileExistCheck(LottoMaxFile) and not fileExistCheck(Lotto649File):
		html = getLottoWinningPage()
	elif not areNumbersRecorded(LottoMaxFile) and not areNumbersRecorded(Lotto649File) and numbersOut():
		html = getLottoWinningPage()
	else:
		html = None
		print("Nothing done.")

	if html:
		lottoMaxNumbers,lotto649Numbers = getLottoNumbers(html) #Parse webpage using regex.

		if lottoMaxNumbers:
			writeToCsvFile(LottoMaxFile, lottoMaxNumbers)
		if lotto649Numbers:
			writeToCsvFile(Lotto649File, lotto649Numbers)
		
		if fileExistCheck(trackFile):
			recordTotal(lottoMaxNumbers, lotto649Numbers)
	else:
		print("TBA")
		sys.exit(1)

def main():
	recordLottoNumbers()
	sys.exit(0)

main()