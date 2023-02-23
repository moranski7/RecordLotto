import csv
from datetime import datetime

target="2023-02-22"

with open("Lotto_Max_Numbers.csv", "r+") as file:
	csvReader = csv.DictReader(file)
	for row in csvReader:
		if row["Date(YYYY-MM-DD)"] == target:
			print("First option. Found date.")
		if target in row.values():
			print("Second option. Found date.")
	file.close()