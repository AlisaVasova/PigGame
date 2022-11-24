from game import PigGame
from player import Player
from unittest.mock import call
from unittest.mock import patch

class PigGameTest(PigGame):
    pass

class MockInputFunction:
    def __init__(self, return_value=None, side_effect=None):
        self.return_value = return_value
        self.side_effect = side_effect
        self.mock_calls = []
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self, prompt=None):
        return_value = self.return_value\
            if self.side_effect is None\
            else self.side_effect[len(self.mock_calls)]
        self.mock_calls.append(call(prompt))
        print(str(return_value))
        return return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn


def test_game_init():
    pl1 = Player("Alice", 2)
    pl2 = Player("Bob", 4)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGame()

    assert game.win_score == 2
    assert game.player_list == [pl1,pl2]
    assert hasattr(game, 'die')
    assert game.roll_counter == 0
    assert game.turn_score == 0

def test_ask_win_score():
    with MockInputFunction(side_effect=["2"]):
        assert PigGame._PigGame__ask_win_score() == 2