def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
=======
Get to the Garden with the key and magic potion to win! Watch out for monsters!
''')

# gotta have that status. Show it!
def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'north': 'Parlor',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Stairs',
    },
    'Parlor': {
        'north': 'Study',
        'south' : 'Hall',
        'west' : 'Library',
        'item' : 'bottle of scotch'
    },
    'Library': {
        'east' : 'Parlor',
        'item' : 'black rifle'
    },
    'Study': {
        'south': 'Parlor',
        'item': 'baseball bat'
    },
    'Kitchen': {
        'north': 'Hall',
        'south' : 'Pantry',
        'item': 'monster'
    },
    'Pantry': {
        'north': 'Kitchen',
        'item' : 'key'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item' : 'monster'
    },
    'Stairs': {
        'east' : 'Hall',
        'west' : 'Basement',
        'item' : 'knife'
    },
    'Basement': {
        'east' : 'Stairs',
        'west' : 'Dungeon',
        'item' : 'monster'
    },
    'Dungeon': {
        'east' : 'Basement',
        'item' : 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if there's a monster in the room, and we have a black rifle, PEW PEW PEW!!!!
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'black rifle' in inventory:
        print("There\'s a monster here!")
        print("You hold your rifle like one of those hipster 3-gun competitors and unload your ")
        print("whole magazine into the monster while shouting, \"PEW PEW PEW!\"")
        print("The monster is swiss cheese! Sadly, you're out of ammo.")
        print("Find a new weapon!")
        del rooms[currentRoom]['item']  # delete the monster from the room
        inventory.remove('black rifle')  # delete black rifle

    # if there's a monster in the room, and we have a bat, WE KILL!!!!!!
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'baseball bat' in inventory:
        print("There\'s a monster here!")
        print("You swing your baseball bat at his head and shout, \"LUCILLE!\"")
        print("The monster dies! You cheer, \"Leroy Jenkins!\"Sadly, your bat, Lucille, is broken in the fight.")
        print("Find a new weapon!")
        del rooms[currentRoom]['item']  # delete the monster from the room
        inventory.remove('baseball bat') # delete baseball bat, I think

    # if there's a monster in the room, and we have a knife, STABBY STABBY TIME!!!!
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'knife' in inventory:
        print("There\'s a monster here!")
        print("You parry as he swipes with his giant, dagger-like claws, ")
        print("and then you lunge with your bowie knife shouting,")
        print("\"That\'s not a knife! THIS IS A KNIFE!!!\" (In an Australian accent, of course).")
        print("The monster dies! Sadly for you, Crocodile Dundee, your giant knife is lodged in his ribs.")
        print("Find a new weapon!")
        del rooms[currentRoom]['item']  # delete the monster from the room
        inventory.remove('knife') # delete baseball bat, I think

    # if there's a monster in the room, and we have a bottle of scotch, SMASH AND STABBY TIME!!!!
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'bottle of scotch' in inventory:
        print("There\'s a monster here!")
        print("Thinking fast, you break your scotch bottle into a shiv and lunge at the monster shouting, ")
        print("What a waste of good scotch!!!\"")
        print("The monster dies! Sadly, your scotch bottle has shattered, ")
        print("and you\'ve wasted good scotch. You\'ll surely go to hell for this.")
        print("Find a new weapon!")
        del rooms[currentRoom]['item']  # delete the monster from the room
        inventory.remove('bottle of scotch')  # delete bottle of scotch... sad day

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster ate your head... GAME OVER!')
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the haunted castle with the special rare key and magic potion... YOU WIN!')
        break
