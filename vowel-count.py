# Write a program that counts the number of vowels in a given string.

text = input("Enter a string: ")
count = 0

for char in text:
    if char.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)
