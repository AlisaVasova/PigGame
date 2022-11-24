from random import randint

class Player:

    def __init__(self, name, order):
        self.name = name
        self.order = order
        if self.name and self.order:
            print(self.name + " присоединяется к игре и получает: " + str(self.order))
        self.score = 0

    def point_counter(self, points):
        try:
            self.score += int(points)
        except ValueError:
            pass
            

class AIPlayer(Player):

    def __init__(self, order=None):
        self.aggressiveness = randint(1, 3)
        super().__init__('computer', order)

    def roll_again(self, turn_score, roll_counter, win_score):
        decision = True
        if self.aggressiveness == 1:
            if turn_score <= 12:
                decision = True
                if self.__more_than_win_score(turn_score, win_score):
                    self.point_counter(turn_score)
                    decision = False
            else:
                self.point_counter(turn_score)
                decision = False
        if self.aggressiveness == 2:
            if (turn_score <= 16) and (roll_counter <= 3):
                decision = True
                if self.__more_than_win_score(turn_score, win_score):
                    self.point_counter(turn_score)
                    decision = False
            else:
                self.point_counter(turn_score)
                decision = False
        if self.aggressiveness == 3:
            if (turn_score <= 20) and (roll_counter <= 5):
                decision = True
                if self.__more_than_win_score(turn_score, win_score):
                    self.point_counter(turn_score)
                    decision = False
            else:
                self.point_counter(turn_score)
                decision = False
        return decision

    def __more_than_win_score(self, add_score, win_score):
        if (self.score + add_score) >= win_score:
            return True
        else:
            return False
