# Designed and built by Daniel Gorelkin IT-140-X2058 23EW2 (11/11/2023)

# Define two options for the menu prompt to be chosen and called by user.
menu_prompt = ('To move: \t\t"N"-north, "S"-south, "E"-east, "W"-west \n'
               'To pick item: \t"Get item name"\n'
               'Instructions: \t"Help"\n'
               'To quit: \t\t"Quit"\n\n')
short_menu_prompt = 'Need help? Just type "Help". Or, "Expand", to get navigation directions.\n'

# Define room specs in a dict. Set by room name, number, item, and adjacent rooms.
rooms = {
    'Lobby': {'name': 'Lobby', 'num': 0, 'item': 'None', 'north': 'History', 'south': 'Math', 'east': 'None',
              'west': 'None'},
    'Social Studies': {'name': 'Social Studies', 'num': 1, 'item': 'phone', 'north': 'None', 'south': 'IT',
                       'east': 'None', 'west': 'None'},
    'IT': {'name': 'IT', 'num': 2, 'item': 'laptop', 'north': 'Social Studies', 'south': 'None', 'east': 'Math',
           'west': 'None'},
    'Math': {'name': 'Math', 'num': 3, 'item': 'calculator', 'north': 'Lobby', 'south': 'None', 'east': 'Physics',
             'west': 'IT'},
    'Chemistry': {'name': 'Chemistry', 'num': 4, 'item': 'beaker', 'north': 'None', 'south': 'Physics', 'east': 'None',
                  'west': 'None'},
    'Physics': {'name': 'Physics', 'num': 5, 'item': 'magnet', 'north': 'Chemistry', 'south': 'None', 'east': 'None',
                'west': 'Math'},
    'History': {'name': 'History', 'num': 6, 'item': 'book', 'north': 'None', 'south': 'Lobby', 'east': 'None',
                'west': 'Chancellor'},
    'Chancellor': {'name': 'Chancellor', 'num': 7, 'item': 'None', 'north': 'None', 'south': 'None', 'east': 'History',
                   'west': 'None'},
    # Define placeholder for room navigation track.
    'Temp_room': {'name': 'Lobby', 'instructions': True},
    'Inventory': {'Social Studies': 'None', 'IT': 'None', 'Math': 'None', 'Chemistry': 'None', 'Physics': 'None',
                  'History': 'None'}
}

# Print the initial main menu and the game commands instructions.
def instructions():
    print("\nWellcome to the Chancellor Text Adventure Quest!\n\n"
          "You must collect all 6 items to win the game before encountering "
          "the chancellor. Otherwise, you will be locked at the campus for one more week.\n"
          "Move commands: 'S' for south, 'N' for north, 'E' for east, 'W' for west\n"
          "Add to Inventory: 'Get & item name'\n"
          "To quit the game: 'Quit'\n"
          "Have a good luck on your journey to escape from SNHU\n")
    # Set pause button to enter the game.
    input("Press Enter to Continue")
    print(23 * "=", end='\n\n')  # Decoration
    main()  # Sends the controls to the commands block.

# Define the current room location print block.
def print_room():
    # Set modular active decoration.
    print()
    print(3*"=", 3*"=", 2*"=", 3*"=", len(rooms[rooms['Temp_room']['name']]['name']) * "=", 5*"=",
          end='\n')
    # Pulls data from global room dict.
    print(f'You are in the', rooms[rooms['Temp_room']['name']]['name'], f'room.')

    # ------------------------------------------------------------------------------------------
    room = rooms['Temp_room']['name']
    room_item = rooms[room]['item']
    if room_item != 'None':
        print('You see a {}.'.format(room_item))
        print('To get it, enter "Get {}".'.format(room_item))
    # ------------------------------------------------------------------------------------------

    # Present inventory on hand and to collect.
    inventory_items = []  # Set list to store collected items
    counter = 0  # Set counter to count collected items
    # Iterate through the items collected from inventory dict
    rooms['Inventory'].values()
    len_counter = 0  # Counter for Underline decoration
    for item in rooms['Inventory'].values():
        if item == 'None':  # Skip uncollected items
            continue
        else:
            len_counter += len(item) + 4
            inventory_items.append(item)  # Add collected items to the list and update counter
            counter += 1  # Present items to be collected
            # If counter reaches '6', means 6 items were collected and the game is over.
            if counter == 6:
                # Print winning statement and quit.
                print('\nCongratulation! You Won and managed to escape from SNHU!\n'
                      'Thanks for playing the game. Hope you enjoyed it.')
                exit()

    print('Your inventory:{} {}/6 collected.'.format(inventory_items, counter))  # Dynamic printout statement.
    print(4 * "=", 9 * "=", len_counter * "=", 14 * "=", end='\n\n')  # Dynamic decoration printout.

# Define the room travel block. Keeps track of room location.
def update_room(c_room, move_room):  # Receives Current room, and direction command.
    if rooms[c_room][move_room] != 'None':  # Validates adjacent room location.
        # If requested room is available, update room location in the global room dict.
        rooms['Temp_room']['name'] = rooms[c_room][move_room]
    else:
        # Print prompt and send back to the command block.
        print("I'm sorry. You can’t go that way!")
        main()
    main()

# define inventory management function 'inventory'
def inventory(room, command):
    tmp_item = rooms[room]['item']
    item = command.split()
    if len(item) == 2 and item[0] == 'get' and item[-1] == tmp_item:
        rooms[room]['item'] = 'None'
        rooms['Inventory'][room] = item[-1]
        input('\nYou got the {}!\n'.format(item[-1]))
        return
    else:
        input('Please type in "Get {}" to pick up the item.'.format(tmp_item))
        main()


# ------------------------------------------------------------------------------------------------------

# Define the game commands block with optional argument reception.
def main(*prompt):
    # Run initial game instructions once only. Could be called through 'help' input.
    if rooms['Temp_room']['instructions']:
        rooms['Temp_room']['instructions'] = False
        instructions()

    # Allows user to set his own prompt menu preferences to be displayed.
    for item in prompt:
        prompt = item

    # Call function to print out current room location
    print_room()
    print("Enter your command:")  # Initial display prompt.

    # User Prompt chooser element. Checks and sets preset or user defined prompt template.
    if prompt == 1:  # Checks if user requested expanded control menu
        text = menu_prompt  # Sets the menu
    else:
        text = short_menu_prompt
    # Read user command input with embedded prompt and store it.
    command = input(text).lower().strip()

    # Command filter block.
    # If navigation commands (e/s/n/w) received, CALL update_room block and send the room and navigation values'''
    if command == 'e':
        update_room(rooms['Temp_room']['name'], 'east')
    elif command == 's':
        update_room(rooms['Temp_room']['name'], 'south')
    elif command == 'n':
        update_room(rooms['Temp_room']['name'], 'north')
    elif command == 'w':
        update_room(rooms['Temp_room']['name'], 'west')
    # Additional commands filter to leave the game, swap prompt or pull initial instructions.
    elif command == 'quit':
        print("\nSo sorry so to see you leaving. See you next round!")
        exit()
    elif command == 'help':
        instructions()
    elif command == 'expand':
        main(1)  # Send change prompt argument to the command block.
    elif 'get' in command:
        inventory(rooms['Temp_room']['name'], command)
        main()
    else:  # Repeat command loop if input is invalid.
        print('\n"' + command + '"' + ' is unrecognized command.')
        main()

# Run program by demand.
if __name__ == '__main__':
    # Call initial instructions block and start the game.
    main()
