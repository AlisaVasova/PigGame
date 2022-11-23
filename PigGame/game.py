# Vincent Lee
# CPSC 386-01
# 2021-10-13
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 01-00
#
# This program has the functions that make up the game 'pig'
#

"""This module is for the PigGame class"""

import time
from dice import Dice
from player import Player
from player import AIPlayer


class PigGame:

    """This is the PigGame class"""

    def __init__(self):
        self.win_score = 100
        self._turn_score = 0
        self._die = Dice()
        self._player_list = self._make_players()
        self._roll_counter = 0
        self._computer = AIPlayer()

    def num_players(self):
        """This function asks for the number of players"""
        num = input("Enter the number of players: ")
        return int(num)

    def ask_single_player(self):
        """Asks if the player would like to play against the computer"""
        ans = input("Would you like to play with the computer? (y/n): ")
        return ans

    def _make_players(self):
        """Organizes the players so they get their order to play"""
        player_list = []
        players = self.num_players()
        if players >= 2:
            for i in range(0, players):
                names = input("Enter name of player {} : ".format(i + 1))
                player_person = Player((names), self._die.roll_die())
                player_list.append(player_person)
                player_list = sorted(
                    player_list, key=lambda order_num: order_num.order
                )
        else:
            # set game for the computer
            names = input("Enter name of player: ")
            player_person = Player((names), self._die.roll_die())
            player_list.append(player_person)
            player_list = sorted(
                player_list, key=lambda order_num: order_num.order
            )
            self._computer = AIPlayer(self._die.roll_die())
            player_list.append(self._computer)
            player_list = sorted(
                player_list, key=lambda order_num: order_num.order
            )
        return player_list

    def print_order_players(self):
        """prints the order of the players"""
        for i in self._player_list:
            print(i.name)

    def hold_turn(self):
        """asks if the player would like to hold"""
        ask_again = True
        while ask_again is True:
            decision = input("Do you wish to hold? (y/n): ")
            if decision == 'y' or decision == 'n':
                ask_again = False
        return decision

    def run_game(self):
        """loop that runs the game"""
        player_score = 0
        while player_score < self.win_score:
            for i in self._player_list:
                turn = 'n'
                self._roll_counter = 0
                self._turn_score = 0
                while turn == 'n':
                    self.seperation_bar()
                    self._die.roll_die()
                    num = self._die.num_roll
                    # print the dice roll
                    print(i.print_name() + " rolls a " + str(num))
                    # add the number of rolls per turn
                    self._roll_counter += 1
                    # display the total score
                    print(
                        "Player's total score of "
                        + i.print_name()
                        + " is "
                        + str(i.score)
                    )
                    print(
                        i.print_name()
                        + "'s number of rolls: "
                        + str(self._roll_counter)
                    )
                    if num != 1:
                        # gets total points of the turn
                        self._turn_score += num
                        # print turn score
                        print(
                            i.print_name()
                            + "'s turn score: "
                            + str(self._turn_score)
                        )
                    else:
                        self._turn_score = 0
                        print(
                            i.print_name()
                            + "'s turn score: "
                            + str(self._turn_score)
                        )
                        print(i.print_name() + " rolled a 0!")
                        time.sleep(2)
                        break
                    time.sleep(2)
                    # Choosing to roll or hold
                    if i.print_name() == self._computer.get_ai_name():
                        ans = self._computer.roll_again(
                            i, self._turn_score, self._roll_counter
                        )
                        if ans is False:
                            turn = 'y'
                            player_score = i.score
                    else:
                        turn = self.hold_turn()
                        if turn == 'y':
                            i.score += self._turn_score
                            player_score = i.score
                if i.score >= self.win_score:
                    winner_name = i.print_name()
                    player_score = i.score
                    break
        self.print_winner(winner_name, player_score)

    @classmethod
    def seperation_bar(cls):
        """creates a seperation line for visualization"""
        print('-------------------------------------')

    @classmethod
    def print_winner(cls, winner, score):
        """prints who the winner is"""
        print('*************************************')
        print("The winner is " + winner + " with " + str(score))
        print('*************************************')

    def run(self):
        """returns 1 that the game is still running"""
        print('Game is running')
        return 1

    def exit(self):
        """lets the players know the game is exiting"""
        self.seperation_bar()
        print('Game is exiting')

    @classmethod
    def exit_code(cls):
        """returns 0 that the game has exited the system"""
        return 0