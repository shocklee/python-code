"""Dice generator.

    This uses the random module to generate random numbers that are closer to
    dice rolls.
    
"""

import random, string

def die(dietype):
    """Roll a single dice.

    Argument controls the size of the dice.
    """

    return random.randrange(1, dietype + 1)

def dice(number, dietype):
    """Roll multiple dice.

    Argument controls the number and size of the dice.
    """
    roll = 0
    for i in range(number):
       roll += die(dietype)
    return roll

def roll(text):
    """Roll multiple dice based upon a text description.

    Argument is a string that describes the number and size of dice along
    with any adjustment to the final roll.  For example, 4d6+1 will generate
    a roll of four six-sided dice and then add one to the final result.  Note
    that this currently only allows an addition or subtaction of a value at
    the end.
    """
    # Convert everything to lower case to make processing easier
    text = string.lower(text)
    index = string.find(text, 'd')
    if index == -1:
        roll = -1  #Error, there was no d in the string
    else:
        dicelist = string.split(text, 'd')  #Split into x and y+z
        if index == 0:
            dicelist[0] = '1'
        # Split into y and z, where z may be a negative number
        dicelist += normalizeroll(dicelist[1])
        roll = dice(int(dicelist[0]), int(dicelist[2])) + int(dicelist[3])
    return roll

def normalizeroll(text):
    """ Normalize the expression to 'y+z', where z may be a negative number

    Argument is a string that describes the size of dice and any adjustment.
    """
    list = string.split(text, '+')
    if len(list) == 1:
        list = string.split(text, '-')
        if len(list) == 1:
            list.append('0')
        else:
            list[1] = '-' + list[1]
    return list


