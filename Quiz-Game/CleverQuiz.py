print("Welcome To The Clever Quiz :-)")
playing = input("Do You Want To Play? ")             
if playing.lower() != "yes":
    quit()
print("Okay! Let's Quiz :)") 

score = 0 

answer = input("What Is The Science Of Colours? ")
if answer.lower() == "chromatics":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later")

answer = input("Blue revolution refers to the production of what? ")
if answer.lower() == "fish":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("Which country has the same flag as USA? ")
if answer.lower() == "liberia":
  print('Yipee Yay, Correct')
  score += 5
else:
  print("Oops, Try Again Later :(")


answer = input("Through which organs do humans produce sound? ")
if answer.lower() == "larynx":
  print('Yipee Yay, Correct') 
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("Where can you find Golden Gate Bridge? ")
if answer.lower() == "san francisco, us":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("What animal is called the 'old man of the sea'? ")
if answer.lower() == "the otter":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("River Volga goes to? ")
if answer.lower() == "caspian sea":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("The river Brahmaputra rises in? ")
if answer.lower() == "manasarovar":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("What Is The roman symbol for number 50? ")
if answer == "L":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("New York City stands on? ")
if answer.lower() == "manhattan island":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("What country was previously known as Indo China? ")
if answer.lower() == "vietnam":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("In what sea does malta lie? ")
if answer.lower() == "the mediterranean":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("What is GPU? ")
if answer.lower() == "graphics processing unit":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later :(")


answer = input("What is CPU? ")
if answer.lower() == "central processing unit":
  print('Yipee Yay, Correct')
  score += 5
else:
    print("Oops, Try Again Later")


answer = input("One planet in the night sky is easily identifiable because of its reddish hue. Which planet? ")
if answer.lower() == "mars":
  print('Yipee Yay, Correct')
  score += 5
else:
  print("Oops, Try Again Later")


print("You got " + str(score) + " Clever quests in all...")
 
print("You had " + str((score/75) * 100) + "% " + "in percentage.")