import random

print("Welcome to the Number Guessing Game! Let's see how many guesses it'll take for you to choose the secret number.")

topOfRange = input("Type a number. This will be the range for the secret number. A smaller number will make the game easier and a larger number will make it more difficult: ")

if topOfRange.isdigit():
  topOfRange = int(topOfRange)

  if topOfRange <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

else:
  print("Please type a number next time.")
  quit()

randomNumber = random.randint(0, topOfRange)
guesses = 0

while True:
  guesses += 1

  userGuess = input("Make a guess: ")

  if userGuess.isdigit():
    userGuess = int(userGuess)
  else:
    print("Please type a number next time.")
    continue

  if userGuess == randomNumber:
    print("Yes, that's right!")
    break
  elif userGuess > randomNumber:
    print("Lower...")
  else:
    print("Higher...")

print("You figured out the secret number in", guesses, "guesses!")