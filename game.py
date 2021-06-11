from map import rooms
from combat import *
from player import *
from items import *
from gameparser import *
from condexit import *
import time



def introduction(curr_room):
    print("LOCATION: WAREHOUSE")
    print("""
Yesterday, ten rebels attacked the nuclear facility in Cornwall at 02:25 am,
and have kept all the employees under hostages. One employee is an undercover
agent working for the crown. Today at 09:50 am, we received intelligence from
one our outfield agents that all the hostages are kept at a research lab just
outside Middlesbrough. Your mission should you choose to accept, is to freed
all the hostages, and bring the agent back safely.


Type ABORT to abort the mission.
Type CONTINUE to continue the mission.

      """)

    user_inputed=input(">")
    normalised=normalise_input(user_inputed)

    if normalised == ['abort']:
        print("You have lost the game")
        exit("game")
    elif normalised == ['continue']:
        return True
    else:
        while normalised !=['abort'] or normalised!=['continue']:
            print("Please enter a valid input")
            user_inputed=input(">")
            normalised=normalise_input(user_inputed)
            if normalised == ['abort']:
                print("You have lost the game")
                exit("game")
            elif normalised == ['continue']:
                return True

def character_creation():
    global firstname
    global lastname
    print("Let's create your character.")
    time.sleep(0.1)
    print("")

    while firstname == "":
        firstname = str(input("Enter your first name: "))
        time.sleep(0.1)
    while lastname == "":
        lastname = str(input("Enter your last name: "))
        time.sleep(0.1)

    print("")
    print(print_character(firstname,lastname))
    print("")

def print_character(first_name,last_name):
    return "PLAYER NAME: "+ first_name.upper() + " "+last_name.upper()

global check
def has_been_visited(room,direction):
    global check
    if direction=="back" and room["items"]==[]:
        check=1
    else:
        check=0

def list_of_items(items):
    global list_items
    """Takes a list of items and returns a comma-seperated list of item names"""
    list_items=[]
    for x in items:
        list_items.append(x["id"])
    return list_items

def print_room(room,items):
    """Takes a room and displays its name and description.
        room is a dictionary"""
    global check
    print("===================================================================================")
    print("")
    if player["health"] > 40:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print(                            "HEALTH:[◼︎◼︎◼︎◼︎◼︎]")

    elif player["health"] > 30 and player["health"] <=40:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print("                           HEALTH:[◼︎◼︎◼︎◼︎ ]")

    elif player["health"] > 20 and player["health"] <=30:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print("                           HEALTH:[◼︎◼︎◼︎  ]")
    elif player["health"] > 10 and player["health"] <=20:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print("                           HEALTH:[◼︎◼︎   ]")
    elif player["health"] > 0 and player["health"] <=10:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print("                           HEALTH:[◼︎    ]")
    elif player["health"] == 0:
        print("BACKPACK [",backpackCount,"| 3] ",end = "")
        if len(list_of_items(items)) != 0:
            for i in range(len(list_of_items(items))):
                print(list_items[i].upper(),end = "|")
        else:
            print("EMPTY | EMPTY | EMPTY ",end = " ")
        print("                           HEALTH:[     ]")

    print("\n")
    print("LOCATION:",room["name"].upper())
    print()
    print(room["description"])

def exit_leads_to(exits,direction):
    """Takes a dictionary of exits and a direction and
       returns the name of the room into which the exit leads"""
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    """Prints a line for the menu of exits"""
    print("GO",direction.upper(),"to",leads_to+".")

def print_menu(exits,room_items,inv_items):
    """Displays the list of possible actions"""
    print()
    print("YOU CAN:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits,direction))
    for item in room_items:
        if room_items!=[]:
            print("TAKE " + item['id'].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        if inv_items!=[]:
            print("DROP " + item['id'].upper() + " to drop " + item["name"] + ".")
    for item in inv_items:
        if inv_items!=[]:
            print("USE " + item['id'].upper() + " to use " + item["name"] + ".")

def can_be_used(item,room):
    """Checks if an item can be used in the current room"""
    global exit_open
    roomlist=[room_bathroom,room_roof,room_trappedRoom,room_vault_locked,room_research,room_warehouse]
    f=0
    if room in roomlist:
        if room==room_bathroom and item == item_wrench["id"]:
            return True
        elif (room == room_roof) and (item== item_rope["id"]) and (item_treasure in inventory):
            exit_open = True
            return False
        elif room ==room_roof and item == item_rope["id"]:
            return True
        elif room == room_trappedRoom and item == item_smoke["id"]:
            return True
        elif room == room_vault_locked and item== item_acid["id"]:
            return True
        elif room == room_research and item== item_key["id"]:
            return True
        elif room == room_warehouse and item== item_uniform["id"]:
            player["health"] += 10
            return True
    return False

def is_valid_exit(exits,chosen_exit):
    """Checks if the chosen exit is a valid exit"""
    return chosen_exit in exits

def execute_go(direction):
    """Updates the current room based on the direction given"""
    global curr_room
    if is_valid_exit(curr_room["exits"], direction):
        curr_room=rooms[curr_room["exits"][direction]]
        has_been_visited(curr_room,direction)
        return curr_room
    else:
        print("You cannot go there")

def execute_take(item):
    """Takes an item and moves it from list of items in curr room
       and moves it to the inventory"""
    global curr_room, inventory, backpackCount
    #backpackCount = 0
    i,f=0,0
    while (i<len(curr_room["items"])) and (backpackCount <= 2):
        if curr_room["items"][i]["id"]==item:
            f+=1
            inventory.append(curr_room["items"][i])
            curr_room["items"].remove(curr_room["items"][i])
            print("You took the " + item + ".")
            backpackCount += 1
        i+=1

    if f==0 or (backpackCount > 2):
        print("You cannot take that!")

def execute_drop(item):
    """Takes an item and moves it from list of items in inventory
       and moves it to the curr room"""
    global curr_room, inventory, backpackCount
    i,f = 0,0
    while (i < len(inventory)):
        if inventory[i]["id"] == item:
            f+=1
            curr_room["items"].append(inventory[i])
            inventory.remove(inventory[i])
            print("You dropped the " + item + ".")
            backpackCount -= 1
        i+=1

    if f==0:
        print("You cannot drop that!")

def execute_use(item):
    """Takes an item and moves it from the inventory to the curr room
       if the item can be used in that room"""

    global curr_room,inventory,backpackCount
    if can_be_used(item,curr_room) == True :
        cond_exit(curr_room,inventory)
        backpackCount -= 1
        i = 0
        while i<len(inventory):
            if inventory[i]['id']==item:
                curr_room['items'].append(inventory[i])
                inventory.remove(inventory[i])
                i+=1

    else:
        print("You can't use it here! Hold onto it!")

def execute_command(command):
    """Takes a command and executes the action requested by the user"""
    if len(command)==0:
        return
    if command[0]=="go":
        if len(command)>1:
            execute_go(command[1])
        else:
            print("Where are you going? ")

    elif command[0]=="take":
        if len(command)>1:
            execute_take(command[1])
        else:
            print("What are you taking? ")

    elif command[0]=="use":
        if len(command)>1:
            execute_use(command[1])
        else:
            print("What are you using? ")
    elif command[0]=="drop":
        if len(command)>1:
            execute_drop(command[1])
        else:
            print("What are you droping? ")

    else:
        print("Please enter a valid action ")

def menu(exits,room_items,inv_items):
    """Takes a dictionary of possible exits, current room items,
       and inventory items and displays the menu of possible actions and exits,
       then asks player to type an action."""
    print_menu(exits, room_items, inv_items)
    print("")
    print("What would you like to do?")
    user_input=input(" > ")
    normalised=normalise_input(user_input)
    return normalised

def main():
    character_creation()
    introduction(curr_room)
    global check, exit_open
    check=0
    while True:
        if item_key in inventory and curr_room['name'] == "Security Booth":
            if combat(player,guard) == "False":
                break

        if curr_room['name']==' Vault':
            player["health"] = 0
            print_room(curr_room,inventory)
            print("You lost!")
            break

        if exit_open == True:
            print("You and the hostages use the rope to escape from the roof")
            time.sleep(2)
            print("")
            print("Congratulations! You have successfully completed the mission!")
            break
        print_room(curr_room,inventory)
#        print_inventory(inventory)
#        cond_exit(curr_room,inventory)
        command=menu(curr_room['exits'],curr_room['items'],inventory)
        print()
        print()
        execute_command(command)
        print()

if __name__ == "__main__":
    main()
