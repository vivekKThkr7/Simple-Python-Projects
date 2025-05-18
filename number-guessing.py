# number-guessing.py

import random

def guess_num():
    secret_num = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < secret_num:
            print("Too low!")
        elif guess > secret_num:
            print("Too high!")
        else:
            print(f"CORRECT! {secret_num} in {attempts} attempts.")
            break
        
if __name__ == "__main__":
    guess_num()
    