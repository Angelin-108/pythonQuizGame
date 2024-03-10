print("WELCOME TO THE QUIZ CHALLENGE")

play = input("Enter YES to continue and NO to quit :")

if play.lower() != "yes":
    quit()

print("Let's start the game")

score = 0

print("1.What is the name of the tallest mountain peak in the world ?")
answer = input("Your answer :")
if answer.lower() == "mount everest":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("2.What is the longest river in the world ?")
answer = input("Your answer :")
if answer.lower() == "nile river":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("3.What is the national bird of India ?")
answer = input("Your answer :")
if answer.lower() == "peacock":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("4.What is the national sport of India ?")
answer = input("Your answer :")
if answer.lower() == "hockey":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("5.What is the most literate state in India ?")
answer = input("Your answer :")
if answer.lower() == "kerala":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("6.What is the largest ocean in the world ?")
answer = input("Your answer :")
if answer.lower() == "pacific ocean":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("7.What is the name of the smallest planet in the solar system ?")
answer = input("Your answer :")
if answer.lower() == "mercury":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("8.What is the name of the most famous painting in the world ?")
answer = input("Your answer :")
if answer.lower() == "mona lisa":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("9.What is the name of the planet that is made up of mostly gas ?")
answer = input("Your answer :")
if answer.lower() == "jupiter":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("10.What is the name of the planet that is made up of mostly rock ?")
answer = input("Your answer :")
if answer.lower() == "earth":
    print("Correct answer")
    score +=1
else:
    print("Wrong answer")

print("Your score is :", score)