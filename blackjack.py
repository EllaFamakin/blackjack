# Use randint to generate random cards. 
from blackjack_helper import *

# USERS'S TURN
player_number = int(input("Welcome to Blackjack! How many players? "))
count = 1
player_list = []
score_dict = {}
while count <= player_number:
  player_name = input("What is player " + str(count) + "'s" + " name? ")
  count += 1
  player_list.append(player_name)
  score_dict[player_name] = [0, 3]

play_again = 'y'
while play_again == 'y':
  for player in player_list:
    user_hand = draw_starting_hand(player + "'s")
    should_hit = 'y'
    while user_hand < 21:
      should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        user_hand = user_hand + draw_card()
    score_dict[player] = [user_hand, score_dict[player][1]]
    print_end_turn_status(user_hand)
  # elif score_dict == {}:
    # break
# DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  


# GAME RESULT
  # list_a = [] 
  print_header('GAME RESULT')
  for player in score_dict.copy():
    total_score = print_end_game_status(score_dict[player][0], player, score_dict[player][1], dealer_hand)
    score_dict[player][1] = total_score
    if score_dict[player][1] == 0:
      print(player + " has been eliminated!")
      player_list.remove(player)
      score_dict.pop(player)
      # list_a.append(player)
  # for i in list_a:
  #     score_dict.pop(i)
  if len(score_dict) == 0:
    print("All players have been eliminated.")
    break
    
      
 
     

  # to repeat the game play
  play_repeat = input("Do you want to play another hand (y/n)? ")
  if play_repeat == 'y':
     play_again = "y"
  elif play_repeat == 'n':
     play_again = 'n'
  else:
     print("Sorry I didn't get that.")