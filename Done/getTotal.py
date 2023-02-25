#This program generates a total times a series of number appears from text file, mods the file, and rewrites to same file using new numbers
#0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

dummyMax = ["02","14","26","31","35","39","49"]
dummy649 = ["03","19","24","25","27","43"]

with open("tracked_Numbers.txt", "r+") as file:
	stringMax = file.readline()
	string649 = file.readline()
	file.close()
numbersMax = [int(x) for x in stringMax.strip().split(",")]
numbers649 = [int(x) for x in string649.strip().split(",")]

for x in dummyMax:
	numbersMax[int(x)] += 1
for x in dummy649:
	numbers649[int(x)] += 1
newNumMax = ",".join(str(x) for x in numbersMax)
newNum649 = ",".join(str(x) for x in numbers649)

print(newNumMax)
print(newNum649)

with open("tracked_numbers.txt", "w") as file:
	file.write(newNumMax)
	file.write("\n")
	file.write(newNum649)
