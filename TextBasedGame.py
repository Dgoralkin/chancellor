# Designed and built by Daniel Gorelkin IT-140-X2058 23EW2 (11/11/2023)


# Define two options for the menu prompt to be chosen and called by user.
menu_prompt = ('To move: \t"N"-north, "S"-south, "E"-east, "W"-west \n'
               'To pick item: \t"Get item name"\n'
               'Instructions: \t"Help"\n'
               'To quit: \t"Quit"\n\n')
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
def show_status():
    # Set modular active decoration.
    print()
    print(3*"=", 3*"=", 2*"=", 3*"=", len(rooms[rooms['Temp_room']['name']]['name']) * "=", 5*"=",
          end='\n')
    # Pulls data from global room dict.
    print(f'You are in the', rooms[rooms['Temp_room']['name']]['name'], f'room.')

    # Pulls room name from dict and stores it in var 'room'
    room = rooms['Temp_room']['name']
    room_item = rooms[room]['item']  # Pulls room item from dict
    if room_item != 'None':  # Validates room item is in the room
        print('You see a {}.'.format(room_item))  # Update prompt
        print('To get it, enter "Get {}".'.format(room_item))  # Instruction prompt

    # Present inventory on hand and to be collected.
    inventory_items = []  # Set list to store collected items
    counter = 0  # Set counter to count collected items
    # Iterate through the items collected from inventory dict
    rooms['Inventory'].values()
    len_counter = 0  # Counter for Underline decoration
    for item in rooms['Inventory'].values():
        if item == 'None':  # Skip uncollected items
            continue
        else:
            len_counter += len(item) + 4  # update counter
            inventory_items.append(item)  # Add collected items to the list and update counter
            counter += 1  # Present items to be collected
            # If counter reaches '6', means 6 items were collected and the game is over.
            if counter == 6:
                # Print winning prompt and quit.
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

        # Set counter to count inventory in the villain room
        inventory_counter = 0
        if rooms['Temp_room']['name'] == 'Chancellor':  # Catch if user enter the villain room
            count = rooms['Inventory'].values()  # Pull items from inventory dict
            for item in count:  # Iterate through the items
                if item != 'None':  # Count how many items were picked up
                    inventory_counter += 1  # Update counter
            if inventory_counter < 6:  # Validate all items were collected
                # If user enter villain room without all the items, print prompt and exit program
                input('\nOh, NO! The Chancellor spotted you without you having all the item handy!'
                      '\nThanks for playing the game. It\'s over. Hope you enjoyed it.')
                exit()
    else:
        # Print prompt and send back to the command block.
        print("\nI'm sorry. You can’t go this way!")
        main()
    main()


# define inventory management function 'inventory' to manage collected item
def inventory(room, command):
    tmp_item = rooms[room]['item']  # Pulls item from dict and stores it in var 'tmp_item'
    item = command.split()  # Splits the input command 'get item_name' and stores it in var
    # Validate 'get item_name was correctly entered by user.'
    if len(item) == 2 and item[0] == 'get' and item[-1] == tmp_item:
        rooms[room]['item'] = 'None'  # Removes the item from its room.
        rooms['Inventory'][room] = item[-1]  # Transfers the item into the inventory dict.
        input('\nYou got the {}!'.format(item[-1]))  # Updates user about the picked up item
        return
    else:
        if room == 'Lobby':  # If user tries to collect item from the Lobby
            # Print prompt for Lobby room and call 'main' function
            print("\nThere are no items to collect from the Lobby. Try another room.")
            main()  # Return to main function
        else:
            input('Please type in "Get {}" to pick up the item.'.format(tmp_item))  # Update message with guidance.
            main()  # Return to main function


# Define main block with optional argument reception.
def main(*prompt):
    # Run initial game instructions once only. Could be called through 'help' input.
    if rooms['Temp_room']['instructions']:
        rooms['Temp_room']['instructions'] = False
        instructions()

    # Allows user to set his own prompt menu preferences to be displayed.
    for item in prompt:
        prompt = item

    # Call function to print out current room location
    show_status()
    print("Enter your command:")  # Initial display prompt.

    # User Prompt chooser element. Checks and sets preset or user defined prompt template.
    if prompt == 1:  # Checks if user requested expanded control menu
        text = menu_prompt  # Sets the menu
    else:
        text = short_menu_prompt  # Sets the menu

    # Call the 'command' function and pass user's optional prompt
    commands(text)


# Define commands block with chosen user prompt.
def commands(text):
    direction = {'e': 'east', 'w': 'west', 'n': 'north', 's': 'south', }
    repeat = True  # Set boolean to run the while loop
    # Run the while loop until valid input is seen
    while repeat:
        command = input(text).lower().strip()  # Read user input command with embedded prompt and store it.
        # Command filter block.
        if command != 'quit':  # For every command besides 'quit' do the following:
            # If navigation commands (e/s/n/w) received, CALL update_room function and pass room + navigation values.
            if command == 'e' or command == 'w' or command == 's' or command == 'n':
                update_room(rooms['Temp_room']['name'], direction[command])

            # Additional commands filter to swap prompt or pull initial instructions.
            elif command == 'help':
                instructions()
            elif command == 'expand':
                main(1)  # Send change prompt argument to the command block.

            # If command is get item: CALL 'inventory' and send args
            elif 'get' in command:
                # call inventory function and pass room name and users' command.
                inventory(rooms['Temp_room']['name'], command)
                # Return to main() if item was picked up successfully.
                main()
            else:  # Repeat command loop if input is invalid.
                print('\n"' + command + '"' + ' is unrecognized command.\nEnter your next command.\n')
        else:
            # If command is 'quit', break the while loop
            repeat = False
            # Print prompt, and end the program.
            print("\nSo sorry to see you leaving. See you next round!")
    exit()

# Run program by demand.
if __name__ == '__main__':
    # Call initial instructions block and start the game.
    main()
