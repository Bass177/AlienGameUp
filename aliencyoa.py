import random as r

from alien_paths import *
from mechanics import *
# game intro screen, add print to display 
print("|---------------------------|\n|-----------Alien-----------|\n|---------------------------|")

#narrative cyoa dialogue 

print(f'You hear hissing, and see nothing but light and then darkness'
'\nThe sound o rushing water ills your ears'
'\nThe light becomes dark'
'\nYou feel weightless, and then . . .'
'\nYou make out a vague humanoid standing over you'
'\nThe ace suddenly changes into a smooth, shiny black oval.'
'\nThere is a ripple, a blur o teeth and snapping jaws . . .'
'\nTHERE IS SCREAMING SCREAMING SCREAMING SCREAMING SCREAMING '
'\n. . .'
'\n. . .'
'\n. . .')

#prompting and storage for player name
#establishes andromeda (think navi for deep space)
p1_name = input(f'WHAT IS YOUR NAME?')


print(f'YOU NEED TO WAKE UP\nWAKE UP' , p1_name.upper() , 'WAKE UP!!!')


PickPath()






