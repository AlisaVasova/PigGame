# Vincent Lee
# CPSC 386-01
# 2021-10-13
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 01-00
#
# This file contains the elements needed for the die
#

"""This module is for the Die class"""

from random import randint

"""This is the Die class"""


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
