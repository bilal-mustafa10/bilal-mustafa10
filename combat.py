import random
import time
import sys
from player import *
alive=True
player = { "health": 40 }
guard = {"health": 40 }


#these lines of text will be printed during combat
combat_text_player = {"You give the guard a right hook to the face dealing", "You headbutt the guard dealing", "You roundhouse kick the guard dealing", "You give the guard a left hook to the chin dealing", "You give the guard the ol' one two dealing"}

combat_text_guard = {"The guard smacks you with his nightstick across the face dealing", "The guard sweeps you off your feet dealing", "Using his nightstick the guard hits the backs of your knees dealing", "The guard winds you with a kick to the chest", "The guard headbutts you dealing"}

#function to initiate combat
def comstart(room, inventory):
    if item_key in inventory and room['name'] == "Security Booth":
        print("The guard has noticed his missing keys and chases after you!")
        return combat(player,guard)


#this function defines the damage the player takes
def take_damage(player):
    damage = 10
    damage = random.randrange(0, damage*2)
    player["health"] = player["health"] - damage
    if player["health"]<0:
        player["health"]=0
    print(random.choice(list(combat_text_guard))+" "+str(damage)+" "+"damage")
    time.sleep(.75)
    print("")
    print("Your health is: " +" "+str(player["health"]))
    print("")
    time.sleep(0.5)
    return
#this function defines the damage the guard takes
def deal_damage(guard):
    player_damage = 9
    player_damage = random.randrange(0, player_damage*2)
    guard["health"] = guard["health"] - player_damage
    if guard["health"]<0:
        guard["health"]=0
    print(random.choice(list(combat_text_player))+" "+str(player_damage) +" "+"damage")
    print("")
    time.sleep(.75)
    print("Guards health:" +" "+str(guard["health"]))
    print("")

#this function defines combat between player and the guard
def combat(player, guard):
    while player["health"] > 0 and guard["health"] > 0:
        print("You fight the guard")
        print("")
        time.sleep(0.5)
        deal_damage(guard)
        time.sleep(1.75)
        if guard["health"] <=0:
            print("You knock the guard out cold and take his keys")
            break
        take_damage(player)
    if guard["health"] <=0:
        time.sleep(0.2)
        return "True"


    elif player["health"] <=0:
        print("The guard knocks you unconscious")

        over = "Game Over.\n"
        for l in over:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.5)
        return "False"
