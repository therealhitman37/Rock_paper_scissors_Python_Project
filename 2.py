#rock, scissors, paper game

import random

def play():
    user = input("What is yout choice? 'r for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r','s','p'])
    print(f"Computer choice is {computer}")
    if user == computer:
        return 'It is a tie'
    elif is_win(user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player,component):
    #return True if player win
    #r>s, s>p, p>r
    if (player== 'r' and component == 's') or (player == 's' and component == 'p') \
        or (player == 'p' and component == 'r'):
        return True
    
print(play())