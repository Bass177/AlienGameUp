
#Player Character
import time as t 
import random as r
r.seed()
class Character():
    def __init__(self, name, max_hp, cur_hp,speed,armor,attack,accuracy,evade) -> None:
        self.name = name
        self.max_hp = max_hp
        self.cur_hp = cur_hp
        self.speed = speed
        self.armor = armor
        self.attack = attack
        self.accuracy = accuracy
        self.evade = evade
# creating a shipmate subclass from Character
class Crewmate(Character):
    def __init__(self, name, max_hp, cur_hp, speed, armor, attack,accuracy,evade) -> None:
        super().__init__(name, max_hp, cur_hp, speed, armor, attack,accuracy,evade)

class Weapons():  
    def __init__(self, name, range,damage,num_uses) -> None:
        self.name = name
        self.range = range 
        self.damage = damage
        self.num_uses = num_uses

# crew weapons
Shotgun = Weapons('Shotgun',2,50,4)
print(Shotgun.damage)  

AutoRifle = Weapons('AutoRifle',5,35,6)
print(AutoRifle.damage)   

Grenade = Weapons('Grenade',4,120,3)
print(Grenade.damage)  

Flamer = Weapons('Flamer',4,80,6)

# Xeno weapons

Slash = Weapons('Slash',1,80,10)
print(Slash.damage)  

TailSlash = Weapons('TailSlash',3,80,10)
print(TailSlash.damage)   

MouthStrike = Weapons('MouthStrike',2,80,10)
print(MouthStrike.damage)  
# acid blood costs 
AcidBlood = Weapons('Flamer',4,120,10)

# creating q Xeno sub-class from the Character 
class Enemy(Character):
    def __init__(self, name, max_hp, cur_hp, speed, armor, attack,accuracy,evade) -> None:
        super().__init__(name, max_hp, cur_hp, speed, armor, attack,accuracy,evade)



# stat scales (1-100,1-100,1-10, 1-100,0-100,1-10)   
Ripley = Crewmate('Ripley',100,100,9,0,1,10,10)

Xenomorph = Enemy('Xenomorph',100,100,9,100,30,8,7)
# def crew and xeno attack

# finish making comparisons for spped. evade, etc....




def XenoAttack():
    print("The Xenomorph moves!")
    attack = r.randint(0,4) 
    print(attack)
    if attack == "1":
        print('The Xeno claws at you!')
        Ripley.cur_hp = Ripley.cur_hp - Slash.damage
        print(Ripley.cur_hp)
    elif attack == "2":
        print("The Xeno strikes with it's tail!")
        Ripley.cur_hp = Ripley.cur_hp - TailSlash.damage
        print(Ripley.cur_hp)
    elif attack == "3":
        print('The Xeno strikes with his tongue!')
        Ripley.cur_hp = Ripley.cur_hp - MouthStrike.damage
        print(Ripley.name , "has" ,Ripley.cur_hp,  " hp left!")
    elif attack == "4":
        print('The Xeno spits acid at you!')
        Ripley.cur_hp = Ripley.cur_hp - AcidBlood.damage
        print(Ripley.cur_hp)
    else:
        print("The xenomorph missed!")   


def RipleyAttack():
    print("Lets kill this bug!")
    print("1." , Shotgun.name , "2." , AutoRifle.name , "3." , Grenade.name , "4." , Flamer.name)
    attack = input("What's your move?")
    if attack == "1":
        print("Ripley fires the shotgun!")
        Xenomorph.cur_hp = Xenomorph.cur_hp - Shotgun.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "2":
        print("Ripley fires the auto rifle!")
        Xenomorph.cur_hp = Xenomorph.cur_hp - AutoRifle.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "3":
        print("Ripley fires the grenade launcher!")
        Xenomorph.cur_hp = Xenomorph.cur_hp - Grenade.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "4":
        print("Ripley fires the flamer!")
        Xenomorph.cur_hp = Xenomorph.cur_hp - Flamer.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    else:
        print("Try again!")
        quit()


    

# creating the move order logic  

def Combat():
    ripley_init = (Ripley.speed + (Ripley.speed * (r.randint(0,1)* 5)))  
    xeno_init = (Xenomorph.speed + (Xenomorph.speed * (r.randint(0,1) * 5))) 
    if ripley_init > xeno_init:
        AccCheckRip()
    elif xeno_init > ripley_init:
        AccCheckXen()
    else: 
        print("Strange times?")
        quit()


    


def AccCheckRip():
    acc_evd_mod = r.randint(0,2)
    if Ripley.accuracy * acc_evd_mod > Xenomorph.evade  * acc_evd_mod:
        t.sleep(4)
        RipleyAttack()
        t.sleep(4)
        print("Got 'em!")
    else:
        print("Missed!")


def AccCheckXen():
    acc_evd_mod = r.randint(0,2)
    if Xenomorph.accuracy * acc_evd_mod > Ripley.evade  * acc_evd_mod:
        t.sleep(4)
        print("SHKREEEEEEEEEEE")
        XenoAttack()
    else:
        print("Missed!")











