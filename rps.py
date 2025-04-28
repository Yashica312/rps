# game bot
import random
def get_computer_choice():
  choices=["rock","paper","scissors"]
  return random.choice(choices)
def get_player_choice():
    player_choice=input("enter a choice:").lower()
    return player_choice
def determine_winner(computer_choice,player_choice):
  if player_choice==computer_choice:
    return "it's a tie!"
  elif ((player_choice=="rock" and computer_choice=="scissors") 
  or (player_choice=="paper" and computer_choice=="rock") or
   (player_choice=="scissors" and computer_choice=="paper")):
    return "you win this round!"
  else:
    return "you lost this round!"
def play_rps():
  print("lets play rock paper scissors!")
  player_score=0
  computer_score=0
  for round in range(3):
    print(f"round{round}:")
    computer_choice=get_computer_choice()
    player_choice=get_player_choice()
    print(f"computer chose:{computer_choice}")
    print(f"you chose:{player_choice}")
    winner=determine_winner(computer_choice,player_choice)
    print(winner)
    if winner=="you win this round!":
      player_score+=1
    elif winner=="you lost this round!":
      computer_score+=1
    print('-'*20)
  if player_score>computer_score:
    print("you win the game")
  elif player_score<computer_score:
    print("you lose the game")
  else:
    print("it's a tie")
  print("game over!!")
play_rps()
