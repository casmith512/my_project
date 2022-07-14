# 
# File: uopsp_assignment3_smicy050
# Author: Christian Smith 
# Email Id: smicy050@mymail.unisa.edu.au 
# Description: Week 8 Question 1
# This is my own work as defined by the University's 
# Academic Misconduct policy. 
#
#
# The following is broken into functions for each of its parts for ease
# of diagnosis.


import random
# This will print the author's details for the user to view once prior
# to the initial menu display.
def display_details():
    # Set details to be the string to be printed
    details = print('File    : uopsp_assignment3_smicy050.py\n'\
                    'Author  : Christian Smith\n'\
                    'Email Id: smicy050\n'\
                    'Date    : 05/06/2022\n'\
                    'Description: Programming Assignment 3 - uopsp\n'\
                    'This is my own work as defined by the University\'s\n'\
                    'Academic Misconduct policy.\n'\
                    )
    return 
# This will read the original textfile in groups of 3 lines.
# The first two ines will be individual list values.
# The last line will be split into 6 list values.
# Once each character is in its own list they will  be combined into
# one list called 'character_list'
def read_file():
    character_file = open('characters.txt','r')  # Open's the character file.
    initial_list = []    # A blank list for the character file.
    character_list = []  # Blank list for character info.
    hero = 0             # Index for assigning each hero.
    initial_list = character_file.readlines()
    while hero < len(initial_list)/3:
        person_list = [] # Each characters list.
        info_index = hero *3 #
        
        while info_index < hero *3 +3:
            char = initial_list[info_index]  # A list for each character.
            char = char.strip()
            if info_index == hero *3 +2:
                char = char.split()
                stat_index = 0  # Index for character stats.
                #split out the stats.
                while stat_index < len (char):
                    stat = char[stat_index]
                    person_list.append(stat)
                    stat_index = stat_index + 1
            else:
                person_list.append(char)
            info_index = info_index + 1
        character_list.append(person_list)
        hero = hero + 1
    character_file.close()
    return (character_list)

# Write_to_file will take any changes that have been made to character_list
# and split out the characters and their stats to the three line setup
# of the input file.
# The output file will be called 'new_characters.txt'.
def write_to_file(outfile,character_list): 
    outfile = open('new_characters.txt','w')  # Open file for writing
    hero_index = 0  # Index for each character
    info_index = 0  # Index for character info
    output = ''     # Blank string for output
    while hero_index < len(character_list):
        info_index = 0
        stats = ''  # String for each characters stats
        while info_index < len(character_list[0]):
            if info_index < 2:
                output = output + '\n'+\
                         str(character_list[hero_index][info_index])
                info_index = info_index + 1
            elif info_index == 7:
                stats = stats + str(character_list[hero_index][info_index])
                info_index = info_index + 1
            else:
                stats = stats + str(character_list[hero_index][info_index])+' '
                info_index = info_index + 1
        output = output.strip()+ '\n' +stats
        hero_index = hero_index + 1
    outfile.write(output)
    outfile.close()
    return

# The topper will concat strings as a display headder.
def topper ():
    double_line = 51*'='  # Line for visual output.
    single_line = '  -\n'+51*'-'  # Line for visual output.
    headder = '\n-'+format('P  W  L  D  Health','>47')  # Stat headdders.
    topper = '\n'+double_line+\
             '\n-     Character (heroes and villains) Summary     -\n'\
             +double_line + headder + single_line+'\n' # Whole headder output.
    return topper

# Each character's stats are passed through this anf formatted for a list.
def char_list_string(character_list,hero_index):
    single_line = '  -\n'+51*'-'
    output = '-  '+format(character_list[hero_index][0],'<26')+\
             format(character_list[hero_index][3],'^3')\
             +format(character_list[hero_index][4],'^3')\
             +format(character_list[hero_index][5],'^3')\
             +format(character_list[hero_index][6],'^3')\
             +format(character_list[hero_index][7],'>7')+single_line
    return output

# Each character's stats are passed through this anf formatted for a list.
# Duplicated function for the copy of the Character list in health.
def char_list_string2(copy_character_list,hero_index):
    single_line = '  -\n'+51*'-'
    output = '-  '+format(copy_character_list[hero_index][0],'<26')+\
             format(copy_character_list[hero_index][3],'^3')\
             +format(copy_character_list[hero_index][4],'^3')\
             +format(copy_character_list[hero_index][5],'^3')\
             +format(copy_character_list[hero_index][6],'^3')\
             +format(copy_character_list[hero_index][7],'>7')+single_line
    return output
    
# This is a validation for character's existance
def find_character(character_list,name):
    search_index = 0  # Index for searching characters
    valid = -1  # Valid is the outout
    while search_index <= len(character_list)-1:
        if str(character_list[search_index][0]) == name:
                valid = search_index
        search_index = search_index + 1
    return valid
    
# This puts together a list of characters.
# Also filters out hroes/villains at the uses request
def display_characters(character_list, display_type):
    double_line = 51*'='
    output = ''  # String for output
    hero_index = 0  # Index for searching characters
    list_vlaue = 'a'  # Dummy value for hero's villains selection
    if display_type == 0:
        list_value = 'all'
    elif display_type == 1:
        list_value = 'v'
    elif display_type == 2:
        list_value = 'h'
    while hero_index <= len(character_list)-1:
        if str(character_list[hero_index][2]) == list_value:
            output = output+ char_list_string(character_list,hero_index)+'\n'
        elif list_value == 'all':
            output = output+ char_list_string(character_list,hero_index)+'\n'
        hero_index = hero_index + 1
    output = topper()+ output +double_line
    print(output+'\n')
    return

# This puts together a list of characters.
# Duplicated function for the copy of the Character list in health
def display_characters2(copy_character_list, display_type):
    double_line = 51*'='  # Line for user output
    output = ''           # String for output
    hero_index = 0        # index for looping through characters
    while hero_index <= len(copy_character_list)-1:
        output = output+ char_list_string2(copy_character_list,hero_index)\
        +'\n'
        hero_index = hero_index + 1
    output = topper()+ output +double_line
    print(output+'\n')
    return

# Search_characters splits outs the users character choice into their
# stats and prints it to the screen
# it will also chech the selections validyt through find_characters
def search_characters(character_list, name):
    search_index = 0  # Index for searching characters
    info = 0          # Int to be used to select the character
    if find_character(character_list,name) <0:
        print('\n'+name+' is not found in character (heroes and villains) '\
              'list.\n')
    elif find_character(character_list,name) >= 0:
          while search_index <= len(character_list)-1:
              if str(character_list[search_index][0]) == name:
                  info = search_index
              search_index = search_index +1
          if character_list[info][2] == 'v':
              hero_type = 'VILLAIN'
          else:
              hero_type = 'HERO'
          print('\nAll about' +name+' --> '+hero_type+'\n')
          print('Secret identity: '+character_list[info][1]+'\n')
          print('Battles fought: '+character_list[info][3])
          print(format('  > No won:','<14')+character_list[info][4])
          print(format('  > No lost:','<14')+character_list[info][5])
          print(format('  > No drawn:','<14')+character_list[info][6]+'\n')
          print('Current health: '+character_list[info][7]+'%\n')

    return
# This will compare each of the characters win count and print back to
# the user the details in a string.
# If two characters have the same win count the highest battle count will win.
def display_highest_battles_won(character_list):
    search_index1 = 0  #Index for searching characters.
    search_index2 = 0  #Index for searching characters.
    highest = -1       #Int to store the highest character.
    hero = -1          #Int to store the character being compared.
    # Loop through each character.
    while search_index2 <= len(character_list)-1:
        # Loop each character through every other character.
        while search_index1 <= len(character_list)-1:
            if int(character_list[search_index1][4]) >= int(highest):
                highest = character_list[search_index1][4]
                hero = search_index1
            search_index1 = search_index1 +1
        # Test if the two chatacters have the same win count.
        if character_list[search_index2][4] == highest\
        and character_list[hero][3] >character_list[search_index2][3]:
            highest = character_list[search_index2][4]
            hero = search_index2
        search_index2 = search_index2 +1
    if highest == -1:
        print('There has been an error')
    else:
        print('\nHighest number of battles won => '+character_list[hero][0]+\
              ' with '+character_list[hero][4]+' opponents defeated!\n')
    return   

# This menu will list the possible inputs for the user and validate them
# returning an error message if incorrect.
def menu():
    # Optinos available to the user for vaidation
    menu_options = ['list', 'heroes', 'villains', 'search', 'reset', \
                    'add', 'remove', 'high','battle', 'health', 'quit']
    # Printed to the user                
    menu_choice = input('Please enter choice\n'\
                '[list, heroes, villains, search, reset, add, remove, high, '\
                'battle, health, quit]: ') 
    while str(menu_choice) not in menu_options:
        print('\nNot a valid command - please try again.\n')
        menu_choice= input('Please enter choice\n'\
                '[list, heroes, villains, search, reset, add, remove, high,'\
                'battle, health, quit]: ')
    output = menu_choice
    return (output)

# Add_character will append the info for a new user to the character list
# It will also print a success message to the user.
def add_character(character_list, name, secret_identity, hero_type):
    new_character = []  # Blank list for new character
    if find_character(character_list,name) >=0:
        print(name+' already exists in character list.')
    else: 
        new_character.append(name)
        new_character.append(secret_identity)
        new_character.append(hero_type)
        new_character.append('0')
        new_character.append('0')
        new_character.append('0')
        new_character.append('0')
        new_character.append('100')
        character_list.append(new_character)
        print('\nSuccessfully added '+name+'to character list\n')
    return character_list

# This will create a new list without the character being removed 
# and send it back to the main menu.
# user input will be validated with find_character.
def remove_character(character_list,name):
    new_character_list = []  # Blank list to be repopulated
    if find_character(character_list,name) <0:
        print(name+' is not found in characters.')
    else:
        number = find_character(character_list,name)  # input validation
        index = 0  # Index for searching characters
        while index < len(character_list):
            if index != number:
                new_character_list.append(character_list[index])
            index = index + 1 
    print('\nSuccessfully removed '+name+' from character list.\n')
    character_list = new_character_list
    return character_list,name

# Battle list will validate the user's input and send back the list index
# and the number of rounds to do battle.
def battle_names(character_list):
    battle_list = []  # Blank list for output
    number1 = -1      # Character 1 list index
    number2 = -2      # Character 2 list index
    rounds = -1       # Nnumber of rounds
    name1 = input('\nPlease enter opponent one\'s name: ')  # User input
    number1 = find_character(character_list,name1)        # Validation
    while int(number1) < 0:
        print('\n'+name1+' is not found in character list '\
              '- please enter another opponent!\n')
        name1 = input('Please enter opponent one\'s name: ')
        number1 = find_character(character_list,name1)
    name2 = input('Please enter opponent two\'s name: ')  # User input
    number2 = find_character(character_list,name2)        # Validation
    while int(number2) < 0: #and int(number2) == int(number1):
        print('\n'+name2+' is not found in character list '\
              '- please enter another opponent!\n')
        name2 = input('Please enter opponent two\'s name: ')
        number2 = find_character(character_list,name2)  
        while int(number1) == int(number2):
            print('\nTwo opponents cannot be the same '\
                  '- please enter another opponent!\n')
            name2 = input('Please enter opponent two\'s name: ')
            number2 = find_character(character_list,name2)
    rounds = input('Please enter number of battle rounds: ')
    while str(rounds) not in ['1','2','3','4','5']:
        print('Must be between 1-5 inclusive.')
        rounds = input('Please enter number of battle rounds: ')
    battle_list.append(number1)
    battle_list.append(number2)
    battle_list.append(rounds)
    return battle_list
    
# Update health updates the health stats for the characters post battle.
# If a characters health is below 0 it will revert to 0
def update_health(character_list, hero, damage):
    character_list[hero][7] = int(character_list[hero][7]) - damage
    if int(character_list[hero][7]) < 0:
        character_list[hero][7] = 0
    remaining_health = int(character_list[hero][7])
    return remaining_health

# Update stats updates the stats for the characters post battle.
def update_stats(character_list,hero,win,loss,draw,battles):
    character_list[hero][3] = str(int(character_list[hero][3]) + battles)
    character_list[hero][4] = str(int(character_list[hero][4]) + win)
    character_list[hero][5] = str(int(character_list[hero][5]) + loss)
    character_list[hero][6] = str(int(character_list[hero][6]) + draw)
    return

# Do battle takes two validated user input characters, randomly assigns
# a damage value between 0 and 50 to be taken away form the characters
# health. Health and win, loss and draw counts are then updated to the
# character list.
# The battle results will be displayed to the user and any deaths reported
def do_battle(character_list, opponent1_pos, opponent2_pos,rounds):
    # List of opponents and rounds for use throughout the functino
    battle_list = [opponent1_pos, opponent2_pos,rounds]
    # Opponents 1 and 2's health stats (pre battle)
    opponent1_health = int(character_list[battle_list[0]][7])
    opponent2_health = int(character_list[battle_list[1]][7])
    rounds = int(battle_list[2]) # Number of rounds
    round_count = 1  # Counting the number of rounds for text output.
    # Print battle results headder
    print('\n-- Battle --\n')
    print(str(character_list[battle_list[0]][0])+' versus '+\
    str(character_list[battle_list[1]][0])+' - '+str(rounds)+' rounds\n')
    # Loop through each round printing the results.
    # Loop will end if the rounds or wither opponents health hits 0
    while rounds > 0 and opponent1_health > 0 and opponent2_health > 0:
        damage1 = random.randint(0,50)
        damage2 = random.randint(0,50)
        opponent1_health = int(update_health(character_list,battle_list[0]\
                               ,damage1))
        opponent2_health = int(update_health(character_list,battle_list[1]\
                               ,damage2))
        print('Round: '+str(round_count))
        print('  > '+str(character_list[battle_list[0]][0])+' Damage: '\
              +str(damage1)+' - Current health: '+str(opponent1_health))
        print('  > '+str(character_list[battle_list[1]][0])+' Damage: '\
              +str(damage2)+' - Current health: '+str(opponent2_health))
        rounds = rounds - 1
        round_count = round_count + 1
    # Print if any characters have died and who was the winner.
    print('\n-- End of battle --')
    if int(opponent1_health) <= 0:
        print('\n-- '+str(character_list[battle_list[0]][0])+\
              ' has died!  :(  ')
    if int(opponent2_health) <= 0:
        print('\n-- '+str(character_list[battle_list[1]][0])+\
              ' has died!  :(  ')
    # Update battle count for each character
    update_stats(character_list,battle_list[0],0,0,0,1)
    update_stats(character_list,battle_list[1],0,0,0,1)
    # Update win loss draw count for each character
    if int(opponent1_health) > int(opponent2_health):
        print('\n** '+str(character_list[battle_list[0]][0])+' wins! **\n')
        update_stats(character_list,battle_list[0],1,0,0,0)
        update_stats(character_list,battle_list[1],0,1,0,0)
    elif int(opponent1_health) < int(opponent2_health):
        print('\n** '+str(character_list[battle_list[1]][0])+' wins! **\n')
        update_stats(character_list,battle_list[0],0,1,0,0)
        update_stats(character_list,battle_list[1],1,0,0,0)
    # Update characters health
    elif int(opponent1_health) == int(opponent2_health):
        print('\n-- A tie. Nobody wins.\n')
        update_stats(character_list,battle_list[0],0,0,1,0)
        update_stats(character_list,battle_list[1],0,0,1,0)
    return

def health_ranking(character_list):

# Health ranking, used in sort by health will compare each characters 
# health stat to see how many others they are better than.
# If there is a tie the most number of battles will decide.
    list_length1 = len(character_list)-1  # Set the maximum loops.
    list_length2 = len(character_list)-1  # Set the maximum loops.
    contender1 = 0   # Defines which character is being used in loop.
    contender2 = 0   # Defines which character is being used in loop.
    worst_list = []  # Output list whith each index corrosponding to a 
                     # character in character_list.
    number = -1      # The number of characters a character is better than.
    # Loop through for each character
    while contender1 <= len(character_list)-1:
        # Loop each character through every other character
        while list_length1 >= 0:
            if int(character_list[contender1][7]) ==\
                int(character_list[contender2][7]):
                if int(character_list[contender1][3]) >=\
                    int(character_list[contender2][3]):
                    number = number + 1
            elif int(character_list[contender1][7]) >=\
                  int(character_list[contender2][7]):
                 number = number + 1
            list_length1 = list_length1 -1
            contender2 = contender2 + 1
        # Append List with number of characters they're better than.
        worst_list.append(len(character_list) -number- 1)
        contender1 = contender1 + 1
        contender2 = 0
        list_length1 = len(character_list)-1
        number = -1
    return worst_list

# Sort by health takes the output list of health_ranking and loop's 
# it through the chatacter list again creating a new list with a new 
# order.
def sort_by_health(character_list):
    ranking = health_ranking(character_list)  # Ranking list
    copy_character_list = []  #Blank list to be appended
    index1 = 0  # Index for loop 1
    index2 = 0  # Index for loop 2
    # Loop for each character.
    while index2 <= len(ranking)-1:
        # Loop through for each character to find their new index in
        # ranking_list
        while index1 <= len(ranking)-1:
            if int(ranking[index1]) == index2:
                copy_character_list.append(character_list[index1])
            index1 = index1 + 1
        index1 = 0
        index2 = index2 + 1
    return copy_character_list

# Character list 2 creats a new list output if there has been a character
# added or removed from the character_list.
# The new character list will remain until the program is quit.
def character_list2(new_character_list):
    character_list = read_file()
    if len(new_character_list) >0:
        append_index = 0
        character_list = []
        while append_index <= len (new_character_list)-1:
            character_list.append(new_character_list[append_index])
            append_index = append_index +1
    return character_list

def user_input():
    user_choice = ''         # User input value string
    new_character_list = []  # Blank list for if the user adds or removes
                             # characters.
    character_list = character_list2(new_character_list)  # Set character list
    # Continue to loop back to menu until user enters 'quit'.
    while user_choice != 'quit':
        # Calls the menu options for the user
        user_choice = menu()
        # Displays a list of all characters and their stats.
        if user_choice == 'list':
             display_characters(character_list,0)
        # Displays a list of all heroes and their stats.
        elif user_choice == 'heroes':
             display_characters(character_list,2)
        # Displays a list of all villains and their stats.
        elif user_choice == 'villains':
             display_characters(character_list,1)
        # Searches and displays a characters stats.
        elif user_choice == 'search':
            name = input('Please enter name: ')
            search_characters(character_list,name)
        # Displays the character with the highest win count
        elif user_choice == 'high':
            display_highest_battles_won(character_list)
        # Adds a new character to the character list
        elif user_choice == 'add':
            name = input('Please enter name: ')
            secret_identity = input('Please enter secret_identity: ')
            hero_type = input('Is this character a hero or a villain [h|v] ')
            if hero_type not in ['h','v']:
                hero_type = input('Is this character a hero or a villain [h|v] ')
            character_list = add_character(character_list, name, secret_identity, \
                                           hero_type)
        # Removes a character from the character list
        elif user_choice == 'remove':
            name = input('Please enter name: ')
            character_list = remove_character(character_list,name)[0]
        # Commits two characters to battle.
        elif user_choice == 'battle':
            battle_list =battle_names(character_list)
            opponent1_pos = battle_list[0]
            opponent2_pos = battle_list[1]
            rounds = battle_list[2]
            do_battle(character_list,opponent1_pos,opponent2_pos,rounds)
        # Displays a list of characters sorted by their current health
        elif user_choice == 'health':
            sort_by_health(character_list)
            copy_character_list = sort_by_health(character_list)
            display_characters2(copy_character_list,0)
        # Resets a characters health to 100.
        elif user_choice == 'reset':
            name = input('\nPlease enter name: ')
            character_list[find_character(character_list,name)][7] = 100
            print('\nSuccessfully updated ' +\
            str(character_list[find_character(character_list,name)][0])+\
            '\'s health to 100\n')
        # Will quit the program and output a text file with any changes
        # made called new_characters.txt.
        elif user_choice == 'quit':
            outfile = 'new_characters.txt'
            write_to_file(outfile,character_list)
    return
        
# Display details to the user
display_details()
user_input()
# Testing git out
# totally real
