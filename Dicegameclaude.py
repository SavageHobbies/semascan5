import random

print("Let's play a dice rolling game!")
player1 = input("Enter name for player 1: ")
player2 = input("Enter name for player 2: ")

def roll_dice():
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  return (roll1, roll2)

def check_win(roll1, roll2):
  if roll1 > roll2:
    return player1
  elif roll2 > roll1:
    return player2
  else:
    return "Tie"

playing = True
while playing:
  roll1, roll2 = roll_dice()
  print(f"{player1} rolled {roll1}") 
  print(f"{player2} rolled {roll2}")
  
  winner = check_win(roll1, roll2)
  if winner != "Tie":
    print(f"{winner} wins!")
    playing = False
  else:
    print("It's a tie! Rolling again...")

print("Thanks for playing!")