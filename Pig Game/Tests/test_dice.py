from dice import Dice

def test_init_dice():
    die = Dice()
    assert die.num_roll == 0

def test_roll_die():
    die = Dice()
    die.roll_die()
    assert die.num_roll <=6 and die.num_roll >=1
