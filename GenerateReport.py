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

def generateImage (numbersAvail,numbersCount, xLabel, imageName):
	import matplotlib.pyplot as plt
	numbersCount.pop(0)
	plt.figure(figsize=(15,6))
	plt.xlabel(xLabel,fontsize=14)
	plt.ylabel("Frequency", fontsize=14)

	plt.bar(numbersAvail, numbersCount,width=0.75)
	plt.savefig(imageName,dpi=400)
	return


def generateReport():
	LottoMaxFile = r"Lotto_Max_Numbers.csv"
	Lotto649File = r"Lotto_649_Numbers.csv"
	trackFile = r"tracked_numbers.txt"

	numbersInMax = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
	"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]
	numbersIn649 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
	"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49"]

	numbersMax,numbers649 = readTotal(trackFile)
	lottoMaxCount = countLinesCSV(LottoMaxFile)
	lott649Count = countLinesCSV(Lotto649File)

	if lottoMaxCount > 0:
		generateImage (numbersInMax, numbersMax, 'Numbers in Lotto Max', "MaxFreq.png")
		avgMax = [(x/lottoMaxCount) for x in numbersMax]

	if lott649Count > 0:
		generateImage (numbersIn649, numbers649, 'Numbers in Lotto 649', "649Freq.png")
		avg649 = [(x/lott649Count) for x in numbers649]

	return

def main():
	generateReport()
	sys.exit(0)

main()