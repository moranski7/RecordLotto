import matplotlib.pyplot as plt

fileName = r"tracked_numbers.txt"

with open(fileName, "r") as file:
	stringMax = file.readline()
	string649 = file.readline()
	file.close()
numbersMax = [int(x) for x in stringMax.strip().split(",")]
print (numbersMax)
numbersMax.pop(0)
print (numbersMax)
numbers649 = [int(x) for x in string649.strip().split(",")]
numbers649.pop(0)

#fig = plt.figure()
numbersInMax = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]
numbersIn649 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49"]
print(len(numbersMax))
print(len(numbersInMax))

plt.figure(figsize=(15,6))
plt.xlabel('Numbers in Lotto Max',fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.bar(numbersInMax, numbersMax,width=0.75)
plt.show()

plt.figure(figsize=(15,6))
plt.xlabel('Numbers in Lotto 649',fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.bar(numbersIn649, numbers649, width=0.75)
plt.show()