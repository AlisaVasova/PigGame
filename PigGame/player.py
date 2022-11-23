from random import randint


class Player:

    def __init__(self, name, order):
        self.__name = name
        self.order = order
        self.joined_game()
        self.score = 0

    def joined_game(self):
        """This function prints out that the player joined and rolled a die"""
        print(
            self.__name + " has joined the game and rolled a: " + str(self.order)
        )

    def print_name(self):
        return self.__name

    def point_counter(self, points):
        self.score += points

    def __repr__(self):
        """prints out python code instead of garbage (good for debugging)"""
        return 'Player("{}", {})'.format(self._name, self.order)


class AIPlayer(Player):

    """This is the AI Player class"""

    def __init__(self, order=None):
        self.ai_name = 'droid56'
        self.aggressiveness = randint(1, 3)
        if order is None:
            self.non_copy_construct()
        else:
            self.copy_construct(order)
        self.ai_score = 0

    @classmethod
    def non_copy_construct(cls):
        """Place holder for the AI player to use it's functionalities"""
        pass

    def copy_construct(self, order):
        """Initiates AI player to join the game"""
        super().__init__(self.ai_name, order)

    def get_ai_name(self):
        """Gets the AI name"""
        return self.ai_name

    def roll_again(self, player_ident, turn_score, roll_counter):
        """How the AI player will play against the player"""
        decision = True
        if self.aggressiveness == 1:
            if turn_score <= 12:
                decision = True
            else:
                player_ident.score += turn_score
                decision = False
        if self.aggressiveness == 2:
            if (turn_score <= 16) and (roll_counter <= 3):
                decision = True
            else:
                player_ident.score += turn_score
                decision = False
        if self.aggressiveness == 3:
            if (turn_score <= 20) and (roll_counter <= 5):
                decision = True
                if (player_ident.score + turn_score) >= 100:
                    player_ident.score += turn_score
                    decision = False
            else:
                player_ident.score += turn_score
                decision = False
        return decision
