from game import PigGame
from player import Player
from player import AIPlayer
from unittest.mock import call
from unittest.mock import patch
import random

class PigGameTest(PigGame):

    def public_make_players(self):
        return self._make_players()

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
    with MockInputFunction(side_effect=["20"]):
        assert PigGame._PigGame__ask_win_score() == 20

def test_ask_win_score_negativ():
    with MockInputFunction(side_effect=["a", "", "0", "20"]):
        assert PigGame._PigGame__ask_win_score() == 20

def test_players_number():
    with MockInputFunction(side_effect=["2"]):
        assert PigGame._PigGame__num_players() == 2

def test_players_number_negativ():
    with MockInputFunction(side_effect=["a", "", "0", "2"]):
        assert PigGame._PigGame__num_players() == 2

@patch('player.Player')
def test_make_players(MockClass):
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGameTest()

    with patch('game.PigGame._PigGame__num_players', side_effect=[2]):
        with patch('dice.Dice.roll_die', side_effect=[4, 2]):
            with MockInputFunction(side_effect=["Alice", "Bob"]):
                with patch('game.PigGame._PigGame__order_players', side_effect=[[pl2, pl1]]):
                    assert game.public_make_players() == [pl2, pl1]

def test_make_players_one_player():
    pl1 = Player("Alice", 4)
    pl2 = AIPlayer(2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGameTest()

    with patch('game.PigGame._PigGame__num_players', side_effect=[1]):
        with patch('dice.Dice.roll_die', side_effect=[4, 2]):
            with MockInputFunction(side_effect=["Alice"]):
                with patch('game.PigGame._PigGame__order_players', side_effect=[[pl2, pl1]]):
                    assert game.public_make_players() == [pl2, pl1]

def test_order_players():
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGame()

    assert game._PigGame__order_players([pl1,pl2]) == [pl2, pl1]

def test_order_players_negativ():
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGame()

    assert game._PigGame__order_players(None) == None

def test_hold_turn():
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]):
        with patch('game.PigGame._make_players', side_effect=[[pl1,pl2]]):
            game = PigGame()

    with MockInputFunction(side_effect=["1", "", "a", "y"]):
        assert game._PigGame__hold_turn() == "y"

def test_game_players():
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[10]):
        with patch('game.PigGame._make_players', side_effect=[[pl2,pl1]]):
            game = PigGame()

    with patch('dice.Dice.roll_die', side_effect=[2, 2, 5, 6]):
        with patch('game.PigGame._PigGame__hold_turn', side_effect=["n", "y", "y", "y"]):
            winner, score = game.run_game()
            assert winner == "Bob"
            assert score == 10

def test_game_play_with_computer():
    pl1 = Player("Alice", 4)
    pl2 = AIPlayer(2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[20]):
        with patch('game.PigGame._make_players', side_effect=[[pl2,pl1]]):
            game = PigGame()

    with patch('dice.Dice.roll_die', side_effect=[3, 4, 6, 5, 5, 5, 5]):
        with patch('player.AIPlayer.roll_again', side_effect=[True, True, False, True, False]):
            with patch('game.PigGame._PigGame__hold_turn', side_effect=["n", "y"]):
                winner, score = game.run_game()
                assert winner == "computer"
                assert score == 23


def test_game_players_with_1():
    pl1 = Player("Alice", 4)
    pl2 = Player("Bob", 2)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[10]):
        with patch('game.PigGame._make_players', side_effect=[[pl2,pl1]]):
            game = PigGame()

    with patch('dice.Dice.roll_die', side_effect=[2, 2, 5, 1, 6, 4]):
        with patch('game.PigGame._PigGame__hold_turn', side_effect=["n", "n", "n", "n", "y"]):
            winner, score = game.run_game()
            assert winner == "Alice"
            assert score == 10


def test_game_init_intgr():
    with MockInputFunction(side_effect=["20", "2", "Alice", "Bob"]):
         with patch('dice.randint', side_effect=[4, 2]):
            game = PigGame()

    assert game.win_score == 20
    assert game.player_list[0].name == "Bob" and game.player_list[0].order == 2 and game.player_list[1].name == "Alice" and game.player_list[1].order == 4
    assert hasattr(game, 'die')
    assert game.roll_counter == 0
    assert game.turn_score == 0

def test_make_players_intgr():
    with MockInputFunction(side_effect=["20", "2", "Alice", "Bob"]):
         with patch('dice.randint', side_effect=[4, 2]):
            game = PigGameTest()

    with MockInputFunction(side_effect=["2", "Alice", "Bob"]):
         with patch('dice.randint', side_effect=[4, 2]):
             assert game.public_make_players() == [pl2, pl1]

def test_game_players_ingr():
    with MockInputFunction(side_effect=["20", "2", "Alice", "Bob"]):
         with patch('dice.randint', side_effect=[4, 2]):
            game = PigGameTest()

    with patch('dice.randint', side_effect=[2, 2, 5, 6]):
        with MockInputFunction(side_effect=["n", "y", "y", "y"]):
            winner, score = game.run_game()
            assert winner == "Bob"
            assert score == 10