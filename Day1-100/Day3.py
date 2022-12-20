#roller-coaster ride

height = int(input("what is your height: "))
age = int(input("enter your age: "))

if height >=120 :
        if age >= 10 and age <= 15:
            print("pay 5$")
        elif age >=16 and age <=20:
            print("pay 7$")
        else:
            print("pay 10$")
else:
        print("not allowed")

#-------------------------------------------------------------------------------------------

#odd-even

number = int(input("enter the number: "))

if number%2==0:
    print("even")
else:
    print("odd")

#-----------------------------------------------------------------------------------------------

weight = int(input("enter your weight: "))
height = float(input("enter your height: "))
BMI = weight/(height*height)


if BMI <= 18.5:
        print("Your BMI is -->",BMI,"and you are underweight")
elif BMI >18.5 and BMI <=25:
    print("Your BMI is -->",BMI,"and you are normal")
elif BMI >25 and BMI <=30:
    print("Your BMI is -->",BMI,"and you are slightly overweight")
elif BMI >30 and BMI <=35:
    print("Your BMI is -->",BMI,"and you are obese")
else:
    print("Your BMI is -->",BMI,"and you are clinically obese")

#=================================================================================

year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆



if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#------------------------------------------------------------------------------------


#pizza-order

size = input("What size of pizza do you want -> S,M or L --->")
add_pepperoni= input("do you want to add pepperoni in your pizza? -> Y or N ")
extra_cheese = input("do you want to add extra cheese in your pizza? -> Y or N  ")

bill = 0

if size=='S':
    bill += 15
elif size =='M':
    bill += 20
elif size == 'L':
    bill += 25


if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    if size == "M" or size == "L":
        bill +=3
else:
    bill = bill

if extra_cheese == "Y":
    bill += 1
else:
    bill = bill


print(f"your final bill is -> ${bill}")

#------------------------------------------------------------------------------------------------------------

#Love calculator

name1 = input("input your the first name here-> ")
name2 = input("input your the second name here-> ")

lower1 = name1.lower()
lower2 = name2.lower()

combined = lower1 + lower2

t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")

true = t+r+u+e

l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e = combined.count("e")

love = l+o+v+e

score = str(true) + str(love)

print(f"your score is -> ${score}")

int_score = int(score)

if int_score <=30:
    print("not that compatible")
elif int_score <=60:
    print("compatible")
elif int_score >=61:
    print("highly compatible")

#------------------------------------------------------------------------------------------------------------------------------

#treasury game

direction = input("where do you want to go? left or right? -> ")

if direction == "left":
    a= input("swim or wait -> ")
    if a == "wait":
        b= input("which door, red, yellow or blue? -> ")
        if b== "yellow":
            print("you win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
