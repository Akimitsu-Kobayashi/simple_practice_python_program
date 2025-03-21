#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# get the users full name and remove leading and 
name = input("Enter your full name: ").strip()

# print the formatted full name
print(f"Your full name is: {name}")