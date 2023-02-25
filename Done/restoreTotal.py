#Read through the csv files and restore the tally. Write to new text file.
import csv
import os

def fileExistCheck(fileName):
	"""Check to see if a file exist. True if yes. False otherwise."""
	return os.path.isfile(fileName)

totalMax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total649 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

if fileExistCheck("Lotto_Max_Numbers.csv"):
	with open("Lotto_Max_Numbers.csv", "r") as csvfile:
		r = csv.DictReader(csvfile)
		for row in r:
			for x in row["Number"].split(","):
				totalMax[int(x)] += 1
		csvfile.close()

if fileExistCheck("Lotto_649_Numbers.csv"):
	with open("Lotto_649_Numbers.csv", "r") as csvfile:
		r = csv.DictReader(csvfile)
		for row in r:
			for x in row["Number"].split(","):
				total649[int(x)] += 1
		csvfile.close()

with open("tracked_Numbers.txt", "w") as file:
	stringMax = ",".join([str(x) for x in totalMax])
	string649 = ",".join(str(x) for x in total649)
	file.write(stringMax)
	file.write("\n")
	file.write(string649)
	file.close()
