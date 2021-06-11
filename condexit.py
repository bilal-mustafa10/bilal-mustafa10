from map import *
from game import *
from player import *

def item_check(itemid, inventory):
    a=0
    for item in inventory:
        if itemid in item['id']:
            a+=1
    return a

def item_remove(itemid, inventory):
    for x in inventory:
        if itemid == x["id"]:
            inventory.remove(x)

def cond_exit(room, inventory):
    global gameCompleted
    roomlist=[room_bathroom,room_roof,room_trappedRoom,room_vault_locked,room_research]
    if room in roomlist:
        if room==room_bathroom:
            if item_check("wrench", inventory) == 1:
                print("""You notice the vent and use your wrench to open it. Your wrench breaks in the process.""")
                room_bathroom["exits"]["up"] = "Vents"
                room_maincorridor["exits"]["up"] = "Vents"
                item_remove("wrench", inventory)
                return
            else:
                return
        elif room==room_roof:
                if item_check("rope",inventory) == 1:
                    global exit_open
                    print("You use your rope to prepare your escape.")
                    exit_open=True
                    item_remove("rope", inventory)
                        #print("You and the hostages use the rope to escape from the roof")
                        #time.sleep(2)
                        #print("")
                        #print("Congratulations! You have successfully completed the mission!")
                else:
                    print("You enjoy the breeze on the roof.")
        elif room==room_trappedRoom:
                if item_check("smoke", inventory) == 1:
                    print("You use the can of smoke in your inventory. The lazers suddenly are visible.")
                    item_remove("smoke", inventory)
                    room_trappedRoom["exits"]["forward"] = "Vault locked"
                else:
                    return
        elif room==room_vault_locked:
                if item_check("acid", inventory) == 1:
                    print("""You set the acid to bore through the doors. The fumes are getting thick.
                    You should GO BACK for a moment.
                    """)
                    curr_room = rooms["Vault unlocked"]
                    room_trappedRoom["exits"]["forward"]="Vault unlocked"
                    item_remove("acid", inventory)
                else:
                    print("The vault is locked.")
                    return
        elif room==room_research:
            if item_check("key", inventory) == 1:
                print("You try the key in the lock. It creaks open - you're in.")
                room_research["exits"]["forward"] = "Main Corridor"
                room_maincorridor["exits"]["back"] = "Main Entrance to the Research Facility"
                item_remove("key", inventory)
    else:
        return
