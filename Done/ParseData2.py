import re
import csv
import os.path
from datetime import datetime

numberPatterns = r"<div class=\"lotto-ball-large selected lotto-ball\"><div class=\"ball-number\">(\d\d)"
lottoMaxPattern = r"alt=\"LOTTO MAX\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
lotto649Pattern = r"alt=\"LOTTO 6/49\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
lottoMaxContents = ""
lotto649Contents = ""
with open("SampleData\\olgWinningPage.txt", "r", encoding="utf-8") as file:
	contents = file.read()
	file.close()

parseResult = re.search(lottoMaxPattern, contents)
lottoMaxNumbers = re.findall(numberPatterns, parseResult.group(0))
fileName = r"Lotto_Max_Numbers.csv"
check_file = os.path.isfile(fileName)
if check_file:
	with open(fileName, "a+") as csvfile:
		fieldnames = ["Number", "Date(YYYY-MM-DD)"]
		w = csv.DictWriter(csvfile, fieldnames=fieldnames)
		numbers = ",".join(lottoMaxNumbers)
		w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
		csvfile.close()
else:
	with open(fileName, "w+") as csvfile:
		fieldnames = ["Number", "Date(YYYY-MM-DD)"]
		w = csv.DictWriter(csvfile, fieldnames=fieldnames)
		w.writeheader()
		numbers = ",".join(lottoMaxNumbers)
		w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
		csvfile.close()

parseResult = re.search(lotto649Pattern, contents)
lotto649Numbers = re.findall(numberPatterns, parseResult.group(0))
fileName = r"Lotto_649_Numbers.csv"
check_file = os.path.isfile(fileName)
if check_file:
	with open(fileName, "a+") as csvfile:
		fieldnames = ["Number", "Date(YYYY-MM-DD)"]
		w = csv.DictWriter(csvfile, fieldnames=fieldnames)
		numbers = ",".join(lotto649Numbers)
		w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
		csvfile.close()
else:
	with open(fileName, "w+") as csvfile:
		fieldnames = ["Number", "Date(YYYY-MM-DD)"]
		w = csv.DictWriter(csvfile, fieldnames=fieldnames)
		w.writeheader()
		numbers = ",".join(lotto649Numbers)
		w.writerow({"Number": numbers, "Date(YYYY-MM-DD)": datetime.today().strftime('%Y-%m-%d')})
		csvfile.close()
