from player import Player
from player import AIPlayer
from unittest.mock import call
from unittest.mock import patch

def test_player_init():
    name = "Alice"
    order = 3
    player1 = Player(name, order)
    assert player1.name == name
    assert player1.order == order
    assert player1.score == 0

def test_player_init_negativ():
    player1 = Player(None, None)
    assert player1.name == None
    assert player1.order == None
    assert player1.score == 0

def test_counter():
    player1 = Player(None, None)
    player1.point_counter(3)
    assert player1.score == 3

def test_counter_negativ():
    player1 = Player(None, None)
    player1.point_counter("a")
    assert player1.score == 0

def test_aiplyer_init_with_order():
    order = 3
    computer = AIPlayer(order)
    assert computer.name == 'computer'
    assert computer.order == order
    assert computer.score == 0
    assert computer.aggressiveness <=3 and computer.aggressiveness >=1

def test_aiplyer_init_with_no_order():
    computer = AIPlayer()
    assert computer.name == 'computer'
    assert computer.order == None
    assert computer.score == 0
    assert computer.aggressiveness <=3 and computer.aggressiveness >=1

def test_roll_again_more_than_win_score():
    computer = AIPlayer()
    computer.score = 23
    turn_score = 12
    roll_counter = 2
    win_score = 30
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[True]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == False

def test_roll_again_aggr1():
    computer = AIPlayer()
    computer.aggressiveness = 1
    computer.score = 5
    turn_score = 10
    roll_counter = 3
    win_score = 30
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[False]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == True

def test_roll_again_aggr2():
    computer = AIPlayer()
    computer.aggressiveness = 2
    computer.score = 5
    turn_score = 14
    roll_counter = 3
    win_score = 30
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[False]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == True

def test_roll_again_aggr3():
    computer = AIPlayer()
    computer.aggressiveness = 3
    computer.score = 5
    turn_score = 20
    roll_counter = 4
    win_score = 30
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[False]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == True

def test_roll_again_big_score():
    computer = AIPlayer()
    computer.score = 5
    turn_score = 22
    roll_counter = 5
    win_score = 30
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[False]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == False

def test_roll_again_negativ():
    computer = AIPlayer()
    computer.score = 5
    turn_score = None
    roll_counter = ""
    win_score = None
    
    with patch('player.AIPlayer._AIPlayer__more_than_win_score', side_effect=[False]):
            assert computer.roll_again(turn_score, roll_counter, win_score) == None

def test_more_than_win_score_is():
    computer = AIPlayer()
    computer.score = 89
    add_score = 12
    win_score = 100
    assert computer._AIPlayer__more_than_win_score(add_score, win_score) == True

def test_more_than_win_score_is_not():
    computer = AIPlayer()
    computer.score = 89
    add_score = 6
    win_score = 100
    assert computer._AIPlayer__more_than_win_score(add_score, win_score) == False

def test_more_than_win_score_negative():
    computer = AIPlayer()
    computer.score = 89
    add_score = None
    win_score = ""
    assert computer._AIPlayer__more_than_win_score(add_score, win_score) == None