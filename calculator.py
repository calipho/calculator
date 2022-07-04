##Enter the first number: 4
##Enter the second number: 6
##Choose the operation (+, -, /, *): *
##The answer is 24


def main():
	firstnumber = input("Enter the first number: ")
	print(firstnumber.isdigit())
	firstnumber = int(firstnumber)
	secondnumber = input("Enter the second number: ")
	print(secondnumber.isdigit())
	secondnumber = int(secondnumber)
	operation = input("Choose the operation (+, -, /, *): ")
	if operation == "*":
		print("The answer is", firstnumber * secondnumber)
	elif operation == "/":
		print("The answer is", firstnumber / secondnumber)
	elif operation == "+":
		print("The answer is", firstnumber + secondnumber)
	elif operation == "-":
		print("The answer is", firstnumber - secondnumber)
	else:
		print("Invalid operation")
	pass
	



if __name__ == '__main__':
	main()
