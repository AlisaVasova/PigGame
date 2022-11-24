from game import PigGame
from player import Player
from unittest.mock import call
from unittest.mock import patch

class PigGameTest(PigGame):
    pass

def test_game_init():
    pl1 = Player("Alice", 2)
    pl2 = Player("Bob", 4)
    with patch('game.PigGame._PigGame__ask_win_score', side_effect=[2]) as __more_than_win_score:
        with patch('game.PigGame._make_players', side_effect=[pl1,pl2]) as point_counter:
            game = PigGame()

    assert game.win_score == 2
    assert game.player_list == [pl1,pl2]
    assert hasattr(game, die)
    assert game.roll_counter == 0
    assert game.turn_score == 0
