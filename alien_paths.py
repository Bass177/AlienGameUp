import random as r 
from mechanics import *
import lorem as l 

# Starting on the Nostromo


def NostromoPath():
    print(l.paragraph)
    print(l.paragraph)
    Combat()
    print(l.paragraph)
    print(l.paragraph)
    Combat()
    print(l.paragraph)
    print(l.paragraph)
    Combat()

# Starting in the egg chamber
def EggChamberPath():
    print(l.paragraph)
# STarting in the vial chamber
def VialChamberPath():
    print(l.paragraph)








def PickPath():
    num = r.random()
    print(num)

    if num <= .33:
        NostromoPath()
    elif num >= .66:
        EggChamberPath()
    else:
        VialChamberPath()



NostromoPath()

