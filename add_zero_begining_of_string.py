#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.


number = int(input("Enter a number (0 - 1000): "))

while number > 1000 or number < 0:
    print(f"The number you have inputed which is ({number}), is not a valid number \nthe progam only accpets number from 0 - 100\n")
    number = int(input("Enter a number (0 - 1000): "))
