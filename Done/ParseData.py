import re

contents = ""
with open("SampleData\\olgWinningPage.txt", "r", encoding="utf-8") as file:
	contents = file.read()
	file.close()

print("LOTTO MAX TEST SET")
print()
print()
print("Test number 1")
print("=====================================================")
pattern = r"alt=\"LOTTO MAX\" class=\"row logo-img\"> <br>[a-zA-Z=\"\-<> \n/\d\,\!\:\.\#\?]*</li> <li><svg aria"
parseResult = re.search(pattern, contents)
print (parseResult.group(0))
print()
print()
print("Test number 2")
print("=====================================================")
pattern = r"alt=\"LOTTO MAX\" class=\"row logo-img\"> <br>[a-zA-Z=\"\-<> \n/\d\,\!\:\.\#\?]*[<li><div class=\"lotto\-ball-large selected lotto\-ball\"><div class=\"ball-number\">]\d\d[</div></div>]*</li> <li><svg aria"
parseResult = re.search(pattern, contents)
print (parseResult.group(0))
print()
print()
print("Test number 3")
print("=====================================================")
pattern = r"alt=\"LOTTO MAX\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
parseResult = re.search(pattern, contents)
print (parseResult.group(0))
print()
print()
print()
print()
print("LOTTO MAX TEST SET")
print()
print()
print("Test number 1")
print("=====================================================")
pattern=r"alt=\"LOTTO 6/49\" class=\"row logo\-img\"> <br>[\n a-zA-Z<>/\d=\"\-\,\!\:\.\#]*Bonus"
parseResult = re.search(pattern, contents)
print (parseResult.group(0))

