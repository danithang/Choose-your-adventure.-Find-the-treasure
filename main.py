print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 
choice1 = input("Which way to the secret treasure 'right' or 'left'? \nChoose wisely or face the consequences. \n").lower()
if choice1 == "right":
  print("Good choice, you can move on")
  #nested if else statement for choice2, if got passed choice1
  choice2 = input("Would you like to swim across immediately or wait for 1 hour for a boat? \nPlease type 'swim' or 'boat'. \n").lower()
  if choice2 == "boat":
    print("Nice!  You are one step closer to the treasure. ")
    
    #nested if, elif, else statement for choice3
    choice3 = input("One more choice, three doors, choose wisely. \nWhich door 'red', 'yellow', or 'blue'? \n").lower()
    if choice3 == ("blue"):
        print("Yay!  You got the treasure.  Congrats!")
    elif choice3 == ("red"):
        print("You just got burned alive in a firey pit! \nBetter luck next time!")
    else:
        print("You chose door yellow \n and you fell into shark infested water and died!  \n Sucks for you!")
  #choice2 else statement if failed choice2
  else:
    print("Sorry, you drowned.  Game Over!")

#choice1 else statement, if choose wrong on choice1 can't go to other choices
else:
  print("Sorry, you fell off a cliff.  Game Over!")


