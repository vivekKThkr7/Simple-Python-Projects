# WAP that generates a random number between 0 and 9 and allows the user to guess it. The user has 5 attempts to guess the number correctly. If they guess correctly, print a congratulatory message. If they fail after 5 attempts, reveal the secret number.


secret = 7
attempts = 0

# Allow up to 5 attempts
while attempts < 5:
    guess = int(input("Guess the number (0-9): "))
    attempts = attempts + 1

    if guess == secret:
        print("Congratulations! You guessed it in", attempts, "attempt(s).")
        break
    else:
        print("Wrong guess. Try again.")

# If loop ends without correct guess, reveal the number
if guess != secret:
    print("Game over. The secret number was", secret)

