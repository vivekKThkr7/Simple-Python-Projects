# Write a program that checks if a number is prime or not.

num = int(input("Enter any number: "))
is_prime = True

if num <2: 
    is_prime = False
    
for i in range(2, num):
    if num % i == 0:
        is_prime = True
        break
    
    
if is_prime:
    print(f"{num} is a Prime Number.")
    
else:
    print(f"{num} is not a Prime Number.")

