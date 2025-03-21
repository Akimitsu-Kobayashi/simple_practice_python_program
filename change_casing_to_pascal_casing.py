#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#get name
name = input("Enter your full name: ").strip()

#get the length of the string including spaces
pascal_casing_name = name.title().replace(" ","")

#print the formatted full name
print(f"your name in pascal case is: {pascal_casing_name}")