# Hack HPC PEARC21
# Voter simulation: Assessing for fair redistricting 

import random as rnd
from typing import Sized

class Voter():
    def __init__(self):
        self.lean = "_"
    
    def __init__(self, lean):
        self.lean = lean
    
    def set_lean(self, voter_lean):
        self.lean = voter_lean

class Community():
    def __init__(self):
        self.voter_list = [] # a community is a collection of voters
        self.voter_districts = [] # a community is also a collection of districts, voters belong in districts
        self.voter_lean_blue = 0
        self.voter_lean_red = 0
        self.voter_lean_grey = 0
    
    def Add_Voter(self, voter):
        self.voter_list.append(voter)
    
    def Add_District(self, district):
        self.voter_districts.append(district)
    
    def Get_Voter_String(self):
        Voter_String = ""
        for v in self.voter_list:
            Voter_String = Voter_String + v.lean
        return Voter_String
    
    def Get_Community_Lean(self):
        self.voter_lean_blue = 0
        self.voter_lean_red = 0
        self.voter_lean_grey = 0
        
        for voter in self.voter_list:
            if voter.lean == "o":
                self.voter_lean_blue = self.voter_lean_blue + 1
            elif voter.lean == "x":
                self.voter_lean_red = self.voter_lean_red + 1
            else:
                self.voter_lean_grey = self.voter_lean_grey + 1
        
        if self.voter_lean_blue >= self.voter_lean_red and self.voter_lean_blue >= self.voter_lean_grey:
            community_lean = "Blue"
        elif self.voter_lean_red >= self.voter_lean_blue and self.voter_lean_red >= self.voter_lean_grey:
            community_lean = "Red"
        elif self.voter_lean_grey >= self.voter_lean_blue and self.voter_lean_grey >= self.voter_lean_red:
            community_lean = "Grey"
        
        return community_lean


#create a random selection of 100 people
#40% chance "+", 30% chance "-", 30% chance "?"
#0-.4 Blue .4-.7 Red .7-1 Grey
#you are *more likely* to be the same color as your neighbor
Person = 0
Blue_Limit = .40
Red_Limit = .70
Grey_Limit = 1
Total_Blues = 0
Total_Reds = 0
Total_Greys = 0
Total_Lean = ""
community = Community()

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
    v = Voter(lean)
    community.Add_Voter(v)
    Blue_Limit = Blue_Limit_New
    Red_Limit = Red_Limit_New
    Grey_Limit = Grey_Limit_New
    Total_Lean = Total_Lean + lean
    Person = Person + 1

print ()
print (community.Get_Voter_String())
print (community.Get_Community_Lean(), community.voter_lean_blue, community.voter_lean_red, community.voter_lean_grey)
print ()

#let's split up our community in smaller communities (i.e. districts)
for i in range(0, 10):
    #define a district
    D = Community()
    #assign the proper voters to the proper district (voters 0 through 9 to District 1, voters 10 through 19 to District 2, etc...)
    D.voter_list = community.voter_list[i*10 : i*10 + 10]
    community.Add_District(D)
    print()
    print (D.Get_Voter_String())
    print (D.Get_Community_Lean())

districts_leaning_blue = 0
districts_leaning_red = 0
districts_leaning_grey = 0
f
or d in community.voter_districts:
    if d.Get_Community_Lean() == "Blue":
        districts_leaning_blue = districts_leaning_blue + 1
    elif d.Get_Community_Lean() == "Red":
        districts_leaning_red = districts_leaning_red + 1
    elif d.Get_Community_Lean() == "Grey":
        districts_leaning_grey = districts_leaning_grey + 1

districts_lean = ""
if districts_leaning_blue >= districts_leaning_red and districts_leaning_blue >= districts_leaning_grey:
    districts_lean = "Blue"
elif districts_leaning_red >= districts_leaning_blue and districts_leaning_red >= districts_leaning_grey:
    districts_lean = "Red"
elif districts_leaning_grey >= districts_leaning_blue and districts_leaning_grey >= districts_leaning_red:
    districts_lean = "Grey"
print()
print (community.Get_Community_Lean(), community.voter_lean_blue, community.voter_lean_red, community.voter_lean_grey)
print (districts_lean, districts_leaning_blue, districts_leaning_red, districts_leaning_grey)
