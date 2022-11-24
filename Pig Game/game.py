import time
from dice import Dice
from player import Player
from player import AIPlayer

class PigGame:

    def __init__(self):
        self.win_score = PigGame._PigGame__ask_win_score()
        self.die = Dice()
        self.player_list = self._make_players()
        self.turn_score = 0
        self.roll_counter = 0

    def __ask_win_score():        
        while True:
            print("Введите количество очков, необходимое для выигрыша: ", end='')
            num = input()
            try:
                if int(num) > 0:
                    return int(num)
                else:
                    print("Ошибка ввода. Попробуйте еще раз.")
            except ValueError:
                print("Ошибка ввода. Попробуйте еще раз.")

    def __num_players():
        while True:
            print("Введите количество игроков: ", end='')
            num = input()
            try:
                if int(num) > 0:
                    return int(num)
                else:
                    print("Ошибка ввода. Попробуйте еще раз.")
            except ValueError:
                print("Ошибка ввода. Попробуйте еще раз.")

    def _make_players(self):
        player_list = []
        players = PigGame._PigGame__num_players()
        if players >= 2:
            for i in range(0, players):
                print("Введите имя игрока {}: ".format(i + 1), end='')
                names = input()
                player_person = Player((names), self.die.roll_die())
                player_list.append(player_person)
        else:
            print("Введите имя игрока: ", end='')
            names = input()
            player_person = Player((names), self.die.roll_die())
            player_list.append(player_person)
            computer = AIPlayer(self.die.roll_die())
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
            for i in self.player_list:
                turn = 'n'
                self.roll_counter = 0
                self.turn_score = 0
                while turn == 'n':
                    self.seperation_bar()       
                    print("Ход игрока " + i.name)
                    num = self.die.roll_die()
                    print(i.name + " выбрасывает: " + str(num))
                    self.roll_counter += 1
                    print(
                        "Общее количество очков: "
                        + str(i.score)
                    )
                    print(
                        "Сделано ходов: "
                        + str(self.roll_counter)
                    )
                    if num != 1:
                        # gets total points of the turn
                        self.turn_score += num
                        # print turn score
                        print(
                            "Можно забрать очков: "
                            + str(self.turn_score)
                        )
                    else:
                        self.turn_score = 0
                        print("Вы теряете набранные очки!")
                        time.sleep(1)
                        break
                    time.sleep(1)
                    # Choosing to roll or hold
                    if isinstance(i, AIPlayer):
                        ans = i.roll_again(self.turn_score, self.roll_counter, self.win_score)
                        if ans is False:
                            turn = 'y'
                            player_score = i.score
                    else:
                        turn = self.__hold_turn()
                        if turn == 'y':
                            i.point_counter(self.turn_score)
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
        