#######################################
# RPG Random Adventure Generator      #
#                                     #
# Based upon the Dungeon Master's     #
#  Design Kit for Advanced Dungeons   #
#  and Dragons by Harold Johnson and  #
#  Aaron Allston.                     #
#                                     #
# Creates random Role-Playing Game    #
#  plot elements for use in creating  #
#  RPG adventures. Based on a fantasy #
#  setting but adaptable to any       #
#  system.                            #
#######################################

import random, sys, csv, getopt, os

#--------------------------------------
# Generate the basic plot of the
# adventure, including:
#    1) Themes
#    2) Goals
#    3) Story Hooks
#    4) General Settings
#    5) Specific Settings
#    6) Allies and Neutrals
#    7) Master Villains
#    8) Minor Villains
#    9) Plots
#    10) Climaxes
#--------------------------------------
def genBasicPlot():

    # Roll for Themes
    myCSV = "basic_plot/themes.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Goals
    myCSV = "basic_plot/goals.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Story Hooks
    myCSV = "basic_plot/story_hooks.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for General Settings
    myCSV = "basic_plot/general_settings.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Specific Settings
    myCSV = "basic_plot/specific_settings.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Allies and Neutrals
    myCSV = "basic_plot/allies_and_neutrals.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Master Villains
    myCSV = "basic_plot/master_villains.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Minor Villains
    myCSV = "basic_plot/minor_villains.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Plots
    myCSV = "basic_plot/plots.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

    # Roll for Climaxes
    myCSV = "basic_plot/climaxes.csv"
    roll = rollPE(myCSV)
    printRoll(roll, myCSV)

#--------------------------------------
# Generate optional plot elements for
# the adventure, including:
#
#    1) Monster Encounters
#    2) Character Encounters
#    3) Traps and Deathtraps
#    4) Special Conditions
#    5) Red Herrings
#    6) Omens and Prophecies
#    7) Moral Quandaries
#    8) Chases
#    9) Secret Weakness
#    10) Cruel Tricks and Complications
#--------------------------------------
def genOptionalPlot():

    # Roll for Monster Encounters
    myCSV = "optional_plot/monster_encounters.csv"
    rollPE(myCSV)

    # Roll for Character Encounters
    myCSV = "optional_plot/character_encounters.csv"
    rollPE(myCSV)

    # Roll for Traps and Deathtraps
    myCSV = "optional_plot/traps_and_deathtraps.csv"
    rollPE(myCSV)

    # Roll for Special Conditions
    myCSV = "optional_plot/special_conditions.csv"
    rollPE(myCSV)

    # Roll for Red Herrings
    myCSV = "optional_plot/red_herrings.csv"
    rollPE(myCSV)

    # Roll for Omens and Prophecies
    myCSV = "optional_plot/omens_and_prophecies.csv"
    rollPE(myCSV)

    # Roll for Moral Quandaries
    myCSV = "optional_plot/moral_quandaries.csv"
    rollPE(myCSV)

    # Roll for Chases
    myCSV = "optional_plot/chases.csv"
    rollPE(myCSV)

    # Roll for Secret Weakness
    myCSV = "optional_plot/secret_weaknesses.csv"
    rollPE(myCSV)

    # Roll for Cruel Tricks and Complications
    myCSV = "optional_plot/cruel_tricks_and_complications.csv"
    rollPE(myCSV)

#--------------------------------------
# Roll the digital dice for
# a plot element defined by input CSV
#--------------------------------------
def rollPE(myCSV):

    roll = random.randint(1,100)
    roll1 = 0
    roll2 = 0

    if myCSV == "basic_plot/themes.csv":
        # When selecting a Theme, a roll
        # 96-100 calls for rolling
        # twice, ignoring further rolls
        # of 96-100
        if roll in range(96,101):
            roll1 = random.randint(1,96)
            roll2 = random.randint(1,96)
    elif myCSV == "basic_plot/specific_settings.csv"\
        or myCSV == "basic_plot/minor_villains.csv":
        # Two rolls are required
        roll1 = random.randint(1,100)
        roll2 = random.randint(1,100)

    # Now lookup the roll value and output
    # resulting theme
    if roll1 == 0:
        output = rollLookup(myCSV, roll)
    else:
        output1 = rollLookup(myCSV, roll1)
        output2 = rollLookup(myCSV, roll2)
        while output1 == output2:
            roll2 = random.randint(1,96)
            output2 = rollLookup(myCSV, roll2)
        output = output1, output2

    return output

#--------------------------------------
# Compare roll value to data with CSV
# designated values for the roll, 
# then output result
#--------------------------------------
def rollLookup(myCSV, myRoll):
    # Read in the appropriate CSV file,
    # find number of rows
    with open(myCSV) as f:
        reader = csv.reader(f, delimiter=",")
        input = list(reader)
        rows = len(input)

    # 1st column of CSV references a range
    # for a die roll - compare our roll
    # value(s) to this range via a list
    rowList = [0]
    
    for i in range(1,rows):
        rowList.append(input[i][0].replace('#', ' ').split(' '))
  
    for i in range(1,rows):
        if myRoll in range(int(rowList[i][0]), int(rowList[i][1])+1):
            output = input[i][1:]
    
    return output

#--------------------------------------
# Print roll results to screen
#--------------------------------------
def printRoll(result, myCSV):

    header, header_length = getCSVinfo(myCSV)

    # Set flag boolean value for a multi-dimensional list
    flag = isinstance(result[0], list)

    # Print column headers and results - if
    # there are two results, print both
    print("\n#####")

    if flag:
        print("\nTwo " + str(header[0][0]) + "s, as follows:")
        for i in range(0,header_length):
            print("\n" + str(header[0][i]) + ": " + str(result[0][i]))
        for i in range(0,header_length):
            print("\n" + str(header[0][i]) + ": " + str(result[1][i]))
    else:
        for i in range(0,header_length):
            print("\n" + str(header[0][i]) + ": " + str(result[i]))

    print("\n#####\n")

#--------------------------------------
# Print roll results to screen
#--------------------------------------
def getCSVinfo(myCSV):
    # Retrieve column headers from CSV
    with open(myCSV) as f:
        reader = csv.reader(f, delimiter=",")
        header = []
        for row in reader:
            header.append(row)
            break   # break after reading first row

    # Delete first column header which references Roll
    del header[0][0]

    # Find how many headers we have for iteration
    header_length = len(header[0])

    return header, header_length

#--------------------------------------
# Generate JSON
#--------------------------------------
def printJSON(optional):
    import json
    from datetime import datetime

    adventure = {}

    # Roll for Themes
    myCSV = "basic_plot/themes.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)

    # Set flag boolean value for a multi-dimensional list
    flag = isinstance(roll[0], list)

    if flag:
        adventure['Themes'] = {}
        adventure['Themes']['Theme 1'] = {}
        adventure['Themes']['Theme 2'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[0][i])}
            adventure['Themes']['Theme 1'].update(update1)
        for i in range(0,header_length):
            update2 = {str(header[0][i]): str(roll[1][i])}
            adventure['Themes']['Theme 2'].update(update2)
    else:
        adventure['Theme'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Theme'].update(update1)

    # Roll for Goals
    myCSV = "basic_plot/goals.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Goal'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Goal'].update(update1)

    # Roll for Story Hooks
    myCSV = "basic_plot/story_hooks.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Story Hook'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Story Hook'].update(update1)

    # Roll for General Settings
    myCSV = "basic_plot/general_settings.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['General Setting'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['General Setting'].update(update1)

    # Roll for Specific Settings
    myCSV = "basic_plot/specific_settings.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Specific Settings'] = {}
    adventure['Specific Settings']['Setting 1'] = {}
    adventure['Specific Settings']['Setting 2'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[0][i])}
        adventure['Specific Settings']['Setting 1'].update(update1)
    for i in range(0,header_length):
        update2 = {str(header[0][i]): str(roll[1][i])}
        adventure['Specific Settings']['Setting 2'].update(update2)

    # Roll for Allies and Neutrals
    myCSV = "basic_plot/allies_and_neutrals.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Allies and Neutrals'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Allies and Neutrals'].update(update1)

    # Roll for Master Villains
    myCSV = "basic_plot/master_villains.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Master Villain'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Master Villain'].update(update1)

    # Roll for Minor Villains
    myCSV = "basic_plot/minor_villains.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Minor Villains'] = {}
    adventure['Minor Villains']['Minor Villain 1'] = {}
    adventure['Minor Villains']['Minor Villain 2'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[0][i])}
        adventure['Minor Villains']['Minor Villain 1'].update(update1)
    for i in range(0,header_length):
        update2 = {str(header[0][i]): str(roll[1][i])}
        adventure['Minor Villains']['Minor Villain 2'].update(update2)

    # Roll for Plots
    myCSV = "basic_plot/plots.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Plot'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Plot'].update(update1)

    # Roll for Climaxes
    myCSV = "basic_plot/climaxes.csv"
    roll = rollPE(myCSV)
    header, header_length = getCSVinfo(myCSV)
    adventure['Climax'] = {}
    for i in range(0,header_length):
        update1 = {str(header[0][i]): str(roll[i])}
        adventure['Climax'].update(update1)

    # Generate optional plot elements if selected
    if optional == True:
        # Roll for Monster Encounters
        myCSV = "optional_plot/monster_encounters.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Monster Encounter'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Monster Encounter'].update(update1)

        # Roll for Character Encounters
        myCSV = "optional_plot/character_encounters.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Character Encounter'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Character Encounter'].update(update1)

        # Roll for Traps and Deathtraps
        myCSV = "optional_plot/traps_and_deathtraps.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Traps and Deathtraps'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Traps and Deathtraps'].update(update1)

        # Roll for Special Conditions
        myCSV = "optional_plot/special_conditions.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Special Conditions'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Special Conditions'].update(update1)

        # Roll for Red Herrings
        myCSV = "optional_plot/red_herrings.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Red Herrings'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Red Herrings'].update(update1)

        # Roll for Omens and Prophecies
        myCSV = "optional_plot/omens_and_prophecies.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Omens and Prophecies'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Omens and Prophecies'].update(update1)

        # Roll for Moral Quandaries
        myCSV = "optional_plot/moral_quandaries.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Moral Quandaries'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Moral Quandaries'].update(update1)

        # Roll for Chases
        myCSV = "optional_plot/chases.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Chases'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Chases'].update(update1)

        # Roll for Secret Weakness
        myCSV = "optional_plot/secret_weaknesses.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Secret Weaknesses'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Secret Weaknesses'].update(update1)

        # Roll for Cruel Tricks and Complications
        myCSV = "optional_plot/cruel_tricks_and_complications.csv"
        roll = rollPE(myCSV)
        header, header_length = getCSVinfo(myCSV)
        adventure['Cruel Tricks and Complications'] = {}
        for i in range(0,header_length):
            update1 = {str(header[0][i]): str(roll[i])}
            adventure['Cruel Tricks and Complications'].update(update1)
        
    # Print adventure to a directory
    my_dir = 'generated_adventures'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, my_dir)
    try:
        os.makedirs(path, exist_ok= True)
    except OSError as error:
        print("Directory '%s' can not be created.\n" % my_dir)

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%y_%H-%M-%S")
    my_name = "adventure_" + dt_string + ".json"
    name2 = os.path.join(path, my_name)

    with open(name2, 'w') as outfile:
        outfile.write(json.dumps(adventure, indent=4))


#######################################
#######################################
def main(argv):

    # Default setting is to only include the basic
    # plot elements. Optional elements can be included
    # through the -o argument.
    optional = False

    # Default setting is to print results to the screen.
    # Changing this setting instead will print to a
    # JSON file, if you're into that sort of thing.
    json = False

    try:
        opts, args = getopt.getopt(argv,"hoj")
    except getopt.GetoptError:
        print('For help, try: adventure_generator.py -h')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('\nadventure_generator.py -h -o -j')
            print('-h : Display this message')
            print('-o : Include optional plot elements')
            print('-j : Print results to JSON file')
            print('\nGenerate an adventure plot for a role-playing game.')
            print('Only a basic plot will be generated by default.')
            print('Include the -o argument to include optional plot elements.\n')
            print('Results are printed to screen by default.')
            print('Include the -j argument to print to JSON instead.')
            sys.exit()
        if opt == '-o':
            optional = True
        if opt == '-j':
            json = True

    # Print to screen by default
    if json == False:
        genBasicPlot()
        # Generate optional plot elements if selected
        if optional == True:
            genOptionalPlot()
    else:
        # Print to JSON file
        printJSON(optional)

#======================================

if __name__ == "__main__":
    main(sys.argv[1:])