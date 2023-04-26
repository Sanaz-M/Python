#We are creating a quiz game(Q&A)


print('Welcome to my game!')

score = 0
playing = input("Do you wanna play? ")

if playing.lower() != 'yes' : 
  quit()
else: 
  print ("Okay! Let's play!")  

#Q1
answer = input("What doese CPU stands for? ")
if answer.lower() == "central processing unit": 
  print('Correct!')
  score += 1
else: 
  print("Incorrect!")

#Q2
answer = input("What doese RAM stands for? ")
if answer.lower() == "random access memory": 
  print('Correct!')
  score += 1
else: 
  print("Incorrect!")

#Q3
answer = input("What doese GPU stands for? ")
if answer.lower() == "graphics processing unit": 
  print('Correct!')
  score += 1
else: 
  print("Incorrect!")

#Q4
answer = input("What doese PSU stands for? ")
if answer.lower() == "power supply": 
  print('Correct!')
  score += 1
else: 
  print("Incorrect!")


print("You answered " + str(score) + " correct")