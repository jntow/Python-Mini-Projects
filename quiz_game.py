print("Welcome to my computer quiz!")

playing = input("Do you want to play? (please answer 'yes' or 'no'): ")
 
if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

print("You earned a score of " + str(score) + " point(s)!")
percentage = (score/4) * 100
if percentage > 50:
  print("Well done! That's " + str(percentage) + " percent!")
elif percentage < 51 and percentage > 0:
  print("Not bad. That's " + str(percentage) + "%.")
else:
  print("Time to do some studying.")