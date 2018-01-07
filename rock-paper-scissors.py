#!/bin/python3

from random import randint

print("******Let's play Rock-Paper-Scissor Game!******\n")

player=input('Type character to choose Rock(r),Paper(p) or Scissors(s)?\n')


chosen=randint(1,3)
#print(chosen)

if(chosen == 1):
	computer = 'r'
elif chosen == 2:
	computer = 'p'
else:
	computer = 's'

print(player, 'vs' ,computer)
if player == computer:
	print('DRAW!')

elif player == 'r' and computer == 's':
	print('Player Wins!')

elif player == 'r' and computer == 'p':
	print('Computer Wins!')

elif player == 'p' and computer == 'r':
	print('Player Wins!')

elif player == 'p' and computer == 's':
	print('Computer Wins!')

elif player == 's' and computer == 'p':
	print('Player Wins!')

elif player == 's' and computer == 'r':
	print('Computer Wins!')