from items import *
from map import rooms

exit_open = False
inventory = []
backpackCount = 0
carrying_weight = 0
firstname=""
lastname=''

# Start game at the reception
curr_room = rooms["Warehouse"]
