import sys
import os
import csv
from datetime import datetime

def fileExistCheck(fileName):
	"""Check to see if a file exist. True if yes. False otherwise."""
	return os.path.isfile(fileName)

def readTotal(fileName):
	try:
		with open(fileName, "r") as file:
			stringMax = file.readline()
			string649 = file.readline()
			file.close()
		numbersMax = [int(x) for x in stringMax.strip().split(",")]
		numbers649 = [int(x) for x in string649.strip().split(",")]
	except FileNotFoundError:
		print("File missing. Please ensure {} is available.".format(fileName))
		#If file does not exist, create new list of zeros for tallying
		numbersMax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		numbers649 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	return numbersMax, numbers649

def countLinesCSV(fileName):

	count = 0
	try:
		with open(fileName, "r") as csvfile:
			r = csv.DictReader(csvfile)
			for row in r:
				count += 1
			csvfile.close()
	except FileNotFoundError:
		print("File missing. Please ensure {} is available.".format(fileName))
		count = 0
	return count

def generateReport():
	LottoMaxFile = r"Lotto_Max_Numbers.csv"
	Lotto649File = r"Lotto_649_Numbers.csv"
	trackFile = r"tracked_numbers.txt"

	numbersMax,numbers649 = readTotal(trackFile)
	lottoMaxCount = countLinesCSV(LottoMaxFile)
	lott649Count = countLinesCSV(Lotto649File)

	avgMax = [(x/lottoMaxCount) for x in numbersMax]
	avg649 = [(x/lott649Count) for x in numbers649]

	return

def main():
	generateReport()
	sys.exit(0)

main()