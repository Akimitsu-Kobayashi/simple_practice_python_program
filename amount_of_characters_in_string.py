#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.

#get name
name = input("Enter your full name: ").strip()

#get the length of the string
amount_of_characters = len(name)

#print the formatted full name
print(f"The amount of characters in your name is: {amount_of_characters}")