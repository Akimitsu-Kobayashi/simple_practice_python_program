#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

#lowercase the string inputted 
statement = input("Enter a complete statement: ").strip()

#counts the spaces in the statement
word_count = statement.count(" ")

#add 1 to word count for it to be counting words and not just the spaces
word_count += 1

#print the formatted full name
print(f"The amount of words in your statement is: {word_count}")