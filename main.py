## ua1a = user action number - day and letter = part of day
import random
predator = random.randint(1,5)
killmonster = random.randint(1,2)
print("Welcome to the Adventure Game!")
print("Make tough decisions to survive")
print("You are stuck on an island! You must survive for 5 days in order to win")
userReady = input("Are you ready?!: ")
if(userReady == "No" or userReady == "no"):
 exit
if(userReady == "yes" or userReady == "Yes"):
 print("You are stuck on an island! You must find some food and survive for today")
 print("Day - 1")
 print("Task: You are hungry and you need some food")
 print("You can do status,food,water, rest")
ua1a = input("What do you want to do?: ")
if(ua1a == "status"):
  print("Health: 100")
  print("Thirst: 100")
  print("Hunger: 100")
  print("Task: You are hungry")
  print("What do you want to do?: ")
if(ua1a == "food"):
  print("you go hunting for food")
  if(predator == 5):
    print("You ran into A Moose while hunting. ")
    if:( )