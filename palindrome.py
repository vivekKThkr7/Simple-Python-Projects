# WAP that checks whether a string is palindrome or not.

name = str(input("Enter a word: "))
if name.lower() == name[::-1].lower():
    print(name, "is a Palindrome.")
else:
    print(name, "is not a Palindrome.")
    
    
    
    
# name = str(input("Enter a word: "))
# reversed = " "

# for str in name:
#     reversed += str
    
# if name == reversed:
#     print(name, " is a Palindrome.")
    
# else:
#     print(name, " is not a Palindrome.")