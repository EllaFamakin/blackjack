# Use randint to generate random cards. 
from random import randint

def rando_card():
      num = randint(1, 13)
      if num == 1:
         print("Drew an Ace")
         num = 11
      elif num > 1 and num <=10 and num != 8:
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

#Generating cards for the starting hand for Dcard_num1
Dcard_num1 = rando_card()
      
#Generating values for the starting hand, Dcard_num2
Dcard_num2 = rando_card()
   
# creating the variable, 'dealer_hand', generating a card for the optional hand, Dcard_num3, and stating conditions for the final hand, BlackJack and bust. 
dealer_hand= Dcard_num1 + Dcard_num2
while dealer_hand < 17:
   print("Dealer has " + str(dealer_hand)+ ".")
   Dcard_num3 = rando_card()
   dealer_hand = dealer_hand + Dcard_num3
   
if dealer_hand >= 17:
   print ("Final hand: "+ str(dealer_hand)+ ".")

if dealer_hand == 21:
   print("BLACKJACK!")
elif dealer_hand > 21:
      print("BUST.")

