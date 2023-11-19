from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

# Prints the given message formatted as a header. 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name + ' TURN')
  return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')

  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(player_hand, players_name, total_score, dealer_hand):
    if player_hand > 21:
      total_score -= 1
      print(players_name + ' loses!' + " score: " + str(total_score))
    elif dealer_hand > 21 and player_hand <= 21:
      total_score += 1
      print(players_name + ' wins!' + " score: " + str(total_score))
    elif player_hand <= 21 and player_hand <= 21:
      if player_hand > dealer_hand:
        total_score += 1
        print(players_name + ' wins!' + " score: " + str(total_score)) 
      elif dealer_hand > player_hand:
        total_score -= 1
        print(players_name + ' loses!' + " score: " + str(total_score))
      else:
         print(players_name + ' Pushes.' + " score: " + str(total_score))
    return total_score
    

# def score_counting(dealer_h, play_h, count_h):
#   if play_h <= 21 and (play_h > dealer_h or dealer_h > 21):
#     count_h += 1
#   elif play_h > 21 or (play_h <= 21 and dealer_h > play_h):
#     count_h -= 1
#   else:
#     count_h == count_h