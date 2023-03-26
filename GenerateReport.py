import sys
import os
import csv
from datetime import datetime

def fileExistCheck(fileName):
	"""Check to see if a file exist. True if yes. False otherwise."""
	return os.path.isfile(fileName)

def initNumberPosList(size, value):
	listNumber = []
	for _ in range(size):
		listNumber.append(value.copy())
	return listNumber

def readTotal(fileName):
	totalMaxRows = 0
	total649Rows = 0
	numMaxPos = []
	num649Pos = []
	totalMax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	total649 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	try:
		with open(fileName, "r") as file:
			totalMaxRows = int(file.readline().strip())
			for _ in range(0,7):
				stringMaxLine = file.readline()
				numMaxPos.append([int(x) for x in stringMaxLine.strip().split(",")])

			total649Rows = int(file.readline().strip())
			for _ in range(0,6):
				string649Line = file.readline()
				num649Pos.append([int(x) for x in string649Line.strip().split(",")])
			file.close()
	except FileNotFoundError:
		print("File missing. Please ensure {} is available.".format(fileName))
		#If file does not exist, create new list of zeros for tallying
		numMaxPos = initNumberPosList (7, totalMax)
		num649Pos = initNumberPosList (6, total649)

	return totalMaxRows, total649Rows, numMaxPos, num649Pos

def generateImage (numbersAvail,numbersCount, xLabel, title,imageName):
	import matplotlib.pyplot as plt
	numbersCount.pop(0)
	plt.figure(figsize=(15,6))
	plt.xlabel(xLabel,fontsize=14)
	plt.ylabel("Frequency", fontsize=14)
	plt.title(title)
	plt.bar(numbersAvail, numbersCount,width=0.75)
	plt.savefig(imageName,dpi=400)
	return

def SuggestNumbers(totalRows, totalPerPos, possibleChoices, numberOfSuggestions):
	import random
	weight = [0 for x in range(0, len(totalPerPos))]
	pickSuggestion = []

	for index in range(0, numberOfSuggestions):
		pick = []
		for row in totalPerPos:
			weight = [((x/totalRows)*100) for x in row]
			number = random.choices(possibleChoices, weights=weight, k=1)
			pick.append(number[0])
		pickSuggestion.append(pick)
	return pickSuggestion

def makeHTML(suggestMax, suggest649):
	with open("Lotto Report.html", "w") as file:
		file.write(r"<!DOCTYPE html>")
		file.write(r"<html>")
		
		file.write("\t<head>")
		file.write("\t<title>Lotto Number Suggestor</title>")
		file.write("<link rel=\"stylesheet\" href=\"report.css\"")
		file.write("\t<meta charset=\"UTF-8\">")
		file.write("\t</head>")
		
		file.write("\t<body>")
		file.write("\t<h1>Lotto Number Suggestor</h1>")
		file.write("\t<table border =\"1\" Class=\"\">")
		
		file.write("\t\t<tr>")
		file.write("\t\t\t<td class=\"Suggestion_Cell\">")
		file.write("\t\t\t<h2>Lotto Max Numbers</h2>")
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggestMax[0])))
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggestMax[1])))
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggestMax[2])))
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggestMax[3])))
		file.write("\t\t\t</td>")
		
		file.write("\t\t\t<td class=\"Suggestion_Cell\">")
		file.write("\t\t\t<h2>Lotto 649 Numbers</h2>")
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggest649[0]))) 
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggest649[1])))
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggest649[2])))
		file.write("\t\t\t<p Class=\"numbers_Suggested\">{}</p>".format(",".join(str(x) for x in suggest649[3])))
		file.write("\t\t\t</td>")
		file.write("\t\t</tr>")


		file.write("\t\t<tr>")
		file.write("\t\t\t<td class=\"Analysis_Cell\">")
		file.write("\t\t\t<h2>Lotto Max Analysis</h2>")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos1.png\" alt=\"Max Numbers Frequency at Position 1\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos2.png\" alt=\"Max Numbers Frequency at Position 2\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos3.png\" alt=\"Max Numbers Frequency at Position 3\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos4.png\" alt=\"Max Numbers Frequency at Position 4\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos5.png\" alt=\"Max Numbers Frequency at Position 5\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos6.png\" alt=\"Max Numbers Frequency at Position 6\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"MaxFreqPos7.png\" alt=\"Max Numbers Frequency at Position 7\">")
		file.write("\t\t\t</td>")
		file.write("\t\t\t<td class=\"Analysis_Cell\">")
		file.write("\t\t\t<h2>Lotto 649 Analysis</h2>")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos1.png\" alt=\"649 Numbers Frequency at Position 1\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos2.png\" alt=\"649 Numbers Frequency at Position 2\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos3.png\" alt=\"649 Numbers Frequency at Position 3\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos4.png\" alt=\"649 Numbers Frequency at Position 4\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos5.png\" alt=\"649 Numbers Frequency at Position 5\">")
		file.write("\t\t\t<img id=\"\" Class=\"barplot\" src=\"649FreqPos6.png\" alt=\"649 Numbers Frequency at Position 6\">")
		file.write("\t\t\t</td>")
		file.write("\t\t</tr>")

		file.write("\t</table>")
		file.write("\t</body>")
		file.write(r"</html>")
		file.close()
	return

def generateReport():
	LottoMaxFile = r"Lotto_Max_Numbers.csv"
	Lotto649File = r"Lotto_649_Numbers.csv"
	trackFile = r"tracked_numbers.txt"

	print("Starting program...")
	numbersInMax = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
	"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]
	numbersIn649 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
	"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49"]

	print("Reading from file...")
	totalMaxRows, total649Rows, numMaxPos, num649Pos = readTotal(trackFile)

	print("Generating images...")
	if totalMaxRows > 0:
		for index in range(0,7):
			generateImage (numbersInMax, numMaxPos[index], 'Numbers in Lotto Max',"Lotto Max Picked Number in Postion {} Frequency".format(index+1),"MaxFreqPos{}.png".format(index+1))
	
	if total649Rows > 0:
		for index in range(0,6):
			generateImage (numbersIn649, num649Pos[index], 'Numbers in Lotto 649',"Lotto 649 Picked Number in Postion {} Frequency".format(index+1),"649FreqPos{}.png".format(index+1))
	
	print("Picking numbers...")
	suggestMax = SuggestNumbers(totalMaxRows, numMaxPos, numbersInMax, 4) #Generate 4 random numbers using weights
	suggest649 = SuggestNumbers(total649Rows, num649Pos, numbersIn649, 4) #Generate 4 random numbers using weights

	print("Creating report...")
	makeHTML(suggestMax, suggest649)
	print("Done.")
	return

def main():
	generateReport()
	sys.exit(0)

main()