#!/user/bin/env python3
# Vincent Lee
# CPSC 386-01
# 2021-10-13
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 01-00
#
# This program executes the game pig!
#

"""This module is the main file to run the game"""

import sys
from game import PigGame


def main():
    """This main starts the loop for the game to start"""
    game = PigGame()
    game.loading()
    game.loaded()
    game.run()
    game.run_game()

    game.exit()
    sys.exit(game.exit_code())


if __name__ == '__main__':
    main()