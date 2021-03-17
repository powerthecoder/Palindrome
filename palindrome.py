# Palindrome will check if the characters in a string are the same backwards
# Coded in python as a one liner

# Code will check for palindrome without symbols
print("No Symbols Allowed"); string = input("Enter The String: "); result = "true" if string[::-1].lower() == string.lower() else "false"; result2 = "No Symbols" if string.isalnum() == False else print(result)

# Code will check for palindrome with any character
string = input("Enter The String: "); result = "true" if string[::-1].lower() == string.lower() else "false"; print(result)
