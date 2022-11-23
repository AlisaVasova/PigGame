from random import randint

class Dice:

    def __init__(self):
        self.num_roll = 0

    def roll_die(self):
        self.num_roll = randint(1, 6)
        return self.num_roll
