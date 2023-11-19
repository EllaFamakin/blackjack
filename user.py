# Use randint to generate random cards. 
from random import randint

def hit_card(): 
    num = randint(1, 13)
    if num == 1:
      print("Drew an Ace")
      num = 11
    elif num > 1 and num <= 10 and num != 8 :
      print ("Drew a " + str(num))
      num = num
    elif num == 8:
      print ("Drew an " + str(num))
      num = num
    elif num == 11:
      print ("Drew a Jack")
      num = 10
    elif num == 12:
      print ("Drew a Queen")
      num = 10
    elif num == 13:
      print ("Drew a King")
      num = 10
    return num

# Generating values to the starting hand, CardNumber1
Ucard_num1 = hit_card()
   
# Generating values for the starting hand, CardNumber2
Ucard_num2 = hit_card()

# creating the variable, 'dealer's hand' 
user_hand= Ucard_num1 + Ucard_num2
while user_hand < 21:
   add_on =(input("You have " + str(user_hand)+ "." + " Hit (y/n)? "))
   if add_on == "y":
# Generating card_num3 if dealer_hand is not up to 17(while loop is employed to acheive this.)
    Ucard_num3 = hit_card()
    user_hand = user_hand + Ucard_num3
   elif add_on == "n":
     print("Final hand: " + str(user_hand)+ ".")
     break
   else:
     print("Sorry I didn't get that.")
 # writing the code to know when to say blackjack or bust and when to stop asking.  
if user_hand >= 21:
   print ("Final hand: "+ str(user_hand)+ ".")

if user_hand == 21:
   print("BLACKJACK!")
elif user_hand > 21:
     print("BUST.")

