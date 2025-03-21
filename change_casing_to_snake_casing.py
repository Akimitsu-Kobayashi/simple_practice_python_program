#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#get name
name = input("Enter your full name: ").strip()

#changes casing to be lower case then replaces each space with a underscore(_)
snake_casing_name = name.lower().replace(" ","_")

#print the formatted full name
print(f"your name in snake case is: {snake_casing_name}")