from random import randint

class Dice:

    """Functions needed for the die"""

    def __init__(self):
        self.num_roll = 0

    def roll_die(self):
        """return the result of the die when rolled"""
        self.num_roll = randint(1, 6)
        return self.num_roll

    def print_roll(self):
        """prints the result of the die"""
        print(self.num_roll)
