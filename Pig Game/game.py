import time
from dice import Dice
from player import Player
from player import AIPlayer


class PigGame:

    def __init__(self):
        self.win_score = self.__ask_win_score()
        self.__turn_score = 0
        self.__die = Dice()
        self.__player_list = self._make_players()
        self.__roll_counter = 0

    def __ask_win_score(self):
        print("Введите количество очков, необходимое для выигрыша: ", end='')
        num = input()
        return int(num)

    def __num_players(self):
        print("Введите количество игроков: ", end='')
        num = input()
        return int(num)

    def _make_players(self):
        player_list = []
        players = self.__num_players()
        if players >= 2:
            for i in range(0, players):
                print("Введите имя игрока {}: ".format(i + 1), end='')
                names = input()
                self.__die.roll_die()
                player_person = Player((names), self.__die.num_roll)
                player_list.append(player_person)
        else:
            # set game for the computer
            print("Введите имя игрока: ", end='')
            names = input()
            self.__die.roll_die()
            player_person = Player((names), self.__die.num_roll)
            player_list.append(player_person)
            self.__die.roll_die()
            computer = AIPlayer(self.__die.num_roll)
            player_list.append(computer)
        player_list = self.__order_players(player_list)
        print("Порядок хода:")
        j = 0
        for i in player_list:
            j += 1
            print(str(j) + ". " + i.name)
        return player_list

    def __order_players(self, player_list):
        return sorted(player_list, key=lambda order_num: order_num.order)

    def __hold_turn(self):
        """asks if the player would like to hold"""
        ask_again = True
        while ask_again is True:
            print("Хотите забрать очки? (y/n): ", end='')
            decision = input()
            if decision == 'y' or decision == 'n':
                ask_again = False
        return decision

    def run_game(self):
        player_score = 0
        while player_score < self.win_score:
            for i in self.__player_list:
                turn = 'n'
                self.__roll_counter = 0
                self.__turn_score = 0
                while turn == 'n':
                    self.seperation_bar()       
                    print("Ход игрока " + i.name)
                    self.__die.roll_die()
                    num = self.__die.num_roll
                    print(i.name + " выбрасывает: " + str(num))
                    self.__roll_counter += 1
                    print(
                        "Общее количество очков: "
                        + str(i.score)
                    )
                    print(
                        "Сделано ходов: "
                        + str(self.__roll_counter)
                    )
                    if num != 1:
                        # gets total points of the turn
                        self.__turn_score += num
                        # print turn score
                        print(
                            "Можно забрать очков: "
                            + str(self.__turn_score)
                        )
                    else:
                        self.__turn_score = 0
                        print(i.name + "Вы теряете набранные очки!")
                        time.sleep(1)
                        break
                    time.sleep(1)
                    # Choosing to roll or hold
                    if isinstance(i, AIPlayer):
                        ans = i.roll_again(self.__turn_score, self.__roll_counter, self.win_score)
                        if ans is False:
                            turn = 'y'
                            player_score = i.score
                    else:
                        turn = self.__hold_turn()
                        if turn == 'y':
                            i.point_counter(self.__turn_score)
                            player_score = i.score
                if i.score >= self.win_score:
                    winner_name = i.name
                    player_score = i.score
                    break

        print('*************************************')
        print("Победителем становится " + winner_name + " с числом очков: " + str(player_score))
        print('*************************************')

    def seperation_bar(self):
        """creates a seperation line for visualization"""
        print('-------------------------------------')

        