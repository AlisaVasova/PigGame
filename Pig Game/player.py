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
        if isinstance(turn_score, int) and isinstance(roll_counter, int) and isinstance(win_score, int):
            if self.__more_than_win_score(turn_score, win_score):
                self.point_counter(turn_score)
                return False
            if self.aggressiveness == 1:
                if turn_score <= 12:
                    return True      
            if self.aggressiveness == 2:
                if (turn_score <= 16) and (roll_counter <= 3):
                    return True
            if self.aggressiveness == 3:
                if (turn_score <= 20) and (roll_counter <= 5):
                    return True
            self.point_counter(turn_score)
            return False
        return None

    def __more_than_win_score(self, add_score, win_score):
        if isinstance(add_score, int) and isinstance(win_score, int):
            if (self.score + add_score) >= win_score:
                return True
            else:
                return False
        return None

