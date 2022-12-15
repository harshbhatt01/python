#particular letter can be taken out from the index number passed in print statement

print("Harsh bhatt a blockchain developer" [8])

#---------------------------------------------------------------------------------------------------------

#Tip calculator

name = input("What is your name: ")
amount_of_bill = int(input("what was your amount of bill: "))
split = int(input("between how many members you want to split the bill: "))
splitted = amount_of_bill/split
print("your name is: ", name, "\nyour amount of bill is: ", amount_of_bill, "\nyou've splitted between: ",split,"members", "\nnow you have to pay: ",splitted)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#addition of string as in number
#-> 27 is a string then indexed by index number and added as int type

digit = (input("keep a number: "))
first = digit[0]
second = digit[1]
third = int(first) + int(second)
print(first ,"+" ,second ,"=", third )

#-----------------------------------------------------------------------------------

#BMI calculator

weight = int(input("enter your weight: "))
height = float(input("enter your height: "))
BMI = weight/(height*height)
print(BMI, "->", int(BMI))

#-----------------------------------------------------------------------------------

#life in weeks

age = int(input("What is your age: "))
days = age * 365
weeks = age * 52
hours = age * 8760

# stats of age-90
days_90 = 90 * 365
weeks_90 = 90 * 52
hours_90 = 90 * 8760

#this will give whatever your age you input , it will say by deducting from age 90 and say what days are left
days_untill_90 = days_90 - days
weeks_untill_90 = weeks_90 - weeks
hours_untill_90 = hours_90 - hours

print("you lived ",days, "days, ",weeks, "weeks and ",hours, "hours") # to print how many days you lived
print("you left ",days_untill_90, "days, ",weeks_untill_90, "weeks and ",hours_untill_90, "hours")# to print how many days left untill you turn 90

#----------------------------------------------------------------------------------------------------------------------------------------------------------

