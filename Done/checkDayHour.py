from datetime import datetime

def numbersOut():
	dt = datetime.now()
	day = dt.strftime('%A')
	hour = dt.hour
	return (day == "Sunday" or day == "Thursday") and (hour > 9)

print("checkDayHour.py")
print("---------------------------------")
print("Note: This test requires tester to change computer clock manually inorder to fully test output.")
print()
print("Test: ")
print("================================")
print(datetime.now().strftime('%A'))
print(datetime.now().hour)
print("Result: ", end="")
print(numbersOut())
print()