import random as rnd
#create a random selection of 100 people
#40% chance "+", 30% chance "-", 30% chance "?"
#you are *more likely* to be the same lean as your neighbor
Person = 0
Blue_Limit = .40
Red_Limit = .70
Grey_Limit = 1
Total_Blues = 0
Total_Reds = 0
Total_Greys = 0
Total_Lean = ""
while Person < 100:
    number = rnd.random()
    if number < Blue_Limit:
        lean = "+"
        Blue_Limit_New = .6
        Red_Limit_New = .8
        Grey_Limit_New = 1
        Total_Blues = Total_Blues + 1
    elif number < Red_Limit:
        lean = "-"
        Blue_Limit_New = .2
        Red_Limit_New = .8
        Grey_Limit_New = 1
        Total_Reds = Total_Reds + 1
    else:
        lean = "?"
        Blue_Limit_New = .2
        Red_Limit_New = .4
        Grey_Limit_New = 1
        Total_Greys = Total_Greys + 1
    Blue_Limit = Blue_Limit_New
    Red_Limit = Red_Limit_New
    Grey_Limit = Grey_Limit_New
    Total_Lean = Total_Lean + lean
    Person = Person + 1
print (Total_Lean)
print (Total_Blues, Total_Reds, Total_Greys)