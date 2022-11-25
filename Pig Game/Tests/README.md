# Тесты

## Блочные тесты
Метод  Dice.__init__ - инициирует экземпляр класса Dice

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_init_dice()``` (инициализация)
  - Входные данные: отсутствуют
  - Ожидаемый результат: свойство num_roll созданного класса равно 0

Метод  Dice.roll_die - имитирует бросание кости

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_roll_die()``` ()
  - Входные данные: self = экземпляр класса Dice
  - Ожидаемый результат: свойство num_roll созданного класса равно 0

Метод  Player.__init__ - инициирует экземпляр класса Player

Аргументы: self - экземпляр класса, в котором выполняется данный метод, name - имя пользователя, order - порядковый номер

 1. Тест ```test_player_init()``` (инициализация)
  - Входные данные: name = "Alice", order = 3
  - Ожидаемый результат: свойство name созданного класса равно "Alice", свойство order созданного класса равно 3, свойство score созданного класса равно 0

 2. Тест ```test_player_init_negativ()``` (негативный - неверные входные данные)
  - Входные данные: name = None, order = None
  - Ожидаемый результат: свойство name созданного класса равно None, свойство order созданного класса равно None, свойство score созданного класса равно 0
  
Метод Player.point_counter - увеличивает количество очков пользователя

Аргументы: self - экземпляр класса, в котором выполняется данный метод, points - количество прибавляемых очков

 1. Тест ```test_counter()``` (инициализация)
  - Входные данные: self = экземпляр класса Player со свойством score равным 0, points = 3
  - Ожидаемый результат: свойство score класса self равно 3

 2. Тест ```test_counter_negativ()``` (негативный - неверные входные данные)
  - Входные данные: self = экземпляр класса Player со свойством score равным 0, points = None
  - Ожидаемый результат: свойство score класса self не изменилось и равно 0
  
Метод  AIPlayer.__init__ - инициирует экземпляр класса AIPlayer

Аргументы: self - экземпляр класса, в котором выполняется данный метод, order - порядковый номер

 1. Тест ```test_aiplayer_init_with_order()``` (инициализация)
  - Входные данные: order = 3
  - Ожидаемый результат: свойство name созданного класса равно 'computer', свойство order созданного класса равно 3, свойство score созданного класса равно 0,  свойство aggressiveness созданного класса <=3 и >=1

 2. Тест ```test_player_init_with_no_order()``` (негативный - неверные входные данные)
  - Входные данные: order = None
  - Ожидаемый результат: свойство name созданного класса равно 'computer', свойство order созданного класса равно None, свойство score созданного класса равно 0,  свойство aggressiveness созданного класса <=3 и >=1
  
Метод AIPlayer.roll_again - высчитывает, забирает ли компьютерный игрок очки или продолжает набирать

Аргументы: self - экземпляр класса, в котором выполняется данный метод, turn_score - число набранных очков, roll_counter - число ходов, win_score - число очков для победы

 1. Тест ```test_roll_again_more_than_win_score()``` (сумма очков больше необходимого для победы)
  - Входные данные: self = экземпляр класса Player со свойством score равным 23, turn_score = 12, roll_counter = 2, win_score = 30
  - Ожидаемый результат: False

 2. Тест ```test_roll_again_aggr1()``` (агрессивность компьютерного игрока равна 1)
  - Входные данные: self = экземпляр класса Player со свойством score равным 5 и свойством aggressiveness равным 1, turn_score = 10, roll_counter = 3, win_score = 30
  - Ожидаемый результат: True
 
 3. Тест ```test_roll_again_aggr2()``` (агрессивность компьютерного игрока равна 2)
  - Входные данные: self = экземпляр класса Player со свойством score равным 5 и свойством aggressiveness равным 2, turn_score = 14, roll_counter = 3, win_score = 30
  - Ожидаемый результат: True
  
 4. Тест ```test_roll_again_aggr3()``` (агрессивность компьютерного игрока равна 3)
  - Входные данные: self = экземпляр класса Player со свойством score равным 5 и свойством aggressiveness равным 3, turn_score = 20, roll_counter = 4, win_score = 30
  - Ожидаемый результат: True
  
 5. Тест ```test_roll_again_big_score()``` (при любой агрессивности число набранных очков достаточно велико для забирания)
  - Входные данные: self = экземпляр класса Player со свойством score равным 5, turn_score = 22, roll_counter = 5, win_score = 30
  - Ожидаемый результат: False

 6. Тест ```test_roll_again_negtiv()``` (негативный - неверные входные данные)
  - Входные данные: self = экземпляр класса Player со свойством score равным 5, turn_score = None, roll_counter = "", win_score = None
  - Ожидаемый результат: None

Метод AIPlayer.__more_than_win_score - высчитывает, станет ли сумма очков после забирания больше или равна требуемой для победы

Аргументы: self - экземпляр класса, в котором выполняется данный метод, add_score - число добавляемых очков, win_score - число очков для победы

 1. Тест ```test_more_than_win_score_is()``` (сумма очков больше или равна необходимого для победы)
  - Входные данные: self = экземпляр класса Player со свойством score равным 89, add_score = 12, win_score = 100
  - Ожидаемый результат: True

 2. Тест ```test_more_than_win_score_is_not()``` (сумма очков меньше необходимого для победы)
  - Входные данные: self = экземпляр класса Player со свойством score равным 89, add_score = 6, win_score = 100
  - Ожидаемый результат: False

 3. Тест ```test_more_than_win_score_negativ()``` (негативный - неверные входные данные)
  - Входные данные: self = экземпляр класса Player со свойством score равным 89, add_score = None, win_score = ""
  - Ожидаемый результат: None

Метод PigGame.__init__ - инициирует экземпляр класса Game

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_game_init()``` (инициализация)
  - Входные данные: отсутсвтуют
  - Ожидаемый результат: свойство win_score созданного класса равно 2; свойство player_list созданного класса является списком пользователей, первый элемент которого - пользователь со свойствами name = "Bob", score = 2, второй пользователь - пользователь со свойствами name = "Alice", score = 4; свойство roll_counter созданного класса равно 0; свойство turn_score созданного класса равно 

Метод PigGame.__ask_win_score - запрашивает у пользователя количество очков для победы

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_ask_win_score()``` (правильный ввод)
  - Входные данные: self = экземпляр класса PigGame, пользователь вводит 20
  - Ожидаемый результат: 20

 2. Тест ```test_ask_win_score_negativ()``` (негативный ввод)
  - Входные данные: self = экземпляр класса PigGame, пользователь вводит "a", "", "0", "20"
  - Ожидаемый результат: 20

Метод PigGame.__players_number - запрашивает у пользователя количество игроков

Аргументы: отсутствуют

 1. Тест ```test_players_number_score()``` (правильный ввод)
  - Входные данные: пользователь вводит 2
  - Ожидаемый результат: 2

 2. Тест ```test_players_number_negativ()``` (негативный ввод)
  - Входные данные: пользователь вводит "a", "", "0", "2"
  - Ожидаемый результат: 2

Метод PigGame._make_players - создает список игроков

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_make_players()``` (правильный ввод - > 1 пользователя)
  - Входные данные: self = экземпляр класса PigGame
  - Ожидаемый результат: список пользователей, первый элемент которого - пользователь со свойствами name = "Bob", score = 2, второй пользователь - пользователь со свойствами name = "Alice", score = 4

 2. Тест ```test_make_players_one_player()``` (правильный ввод - 1 пользователь)
  - Входные данные: self = экземпляр класса PigGame
  - Ожидаемый результат: список пользователей, первый элемент которого - пользователь со свойствами name = "computer", score = 2, второй пользователь - пользователь со свойствами name = "Alice", score = 4

Метод PigGame.game - процесс игры

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_game_players()``` (> 1 игрока)
  - Входные данные: self = экземпляр класса PigGame с двумя пользователями: name = "Bob", score = 2; name = "Alice", score = 4
  - Ожидаемый результат: "Bob", 10

 2. Тест ```test_game_play_with_computer()``` (игра с компьютером)
  - Входные данные: self = экземпляр класса PigGame с двумя пользователями: name = "computer", score = 2; name = "Alice", score = 4
  - Ожидаемый результат: "computer", 23
  
## Интеграционные тесты 

Метод AIPlayers.roll_again() вызывает функцию AIPlayers.__more_than_win_score

Аргументы: self - экземпляр класса, в котором выполняется данный метод, turn_score - число набранных очков, roll_counter - число ходов, win_score - число очков для победы

1. Тест ```test_roll_again_intgr``` (есть решение для данной задачи)
  - Входные данные: self = экземпляр класса Player со свойством score равным 23, turn_score = 12, roll_counter = 2, win_score = 30
  - Ожидаемый результат: False
 
Метод PigGame.game() вызывает функции: PigGame.__ask_win_score, PigGame._make_players, AIPlayer.roll_again, PigGame._PigGame__hold_turn

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_game_players_intgr()``` (> 1 игрока)
  - Входные данные: self = экземпляр класса PigGame с двумя пользователями: name = "Bob", score = 2; name = "Alice", score = 4, пользователь вводит "n", "y", "y", "y"
  - Ожидаемый результат: "Bob", 10

 2. Тест ```test_game_play_with_computer_intgr()``` (игра с компьютером)
  - Входные данные: self = экземпляр класса PigGame с двумя пользователями: name = "computer", score = 2; name = "Alice", score = 4, пользователь вводит "n", "y"
  - Ожидаемый результат: "computer", 23

Метод PigGame.__init__ вызывает функции PigGame.__ask_win_score(), PigGame._make_players()

Аргументы: self - экземпляр класса, в котором выполняется данный метод

 1. Тест ```test_game_init_intgr()``` (инициализация)
  - Входные данные: пользователь вводит "20", "2", "Alice", "Bob"
  - Ожидаемый результат: свойство win_score созданного класса равно 2; свойство player_list созданного класса является списком пользователей, первый элемент которого - пользователь со свойствами name = "Bob", score = 2, второй пользователь - пользователь со свойствами name = "Alice", score = 4; свойство roll_counter созданного класса равно 0; свойство turn_score созданного класса равно 

## Аттестационные тесты 

1. Тест 1 - проверка запуска программы
 - Действия: пользователь запускает программу
 - Ожидаемый результат: программа запрашивает количество баллов для победы
 
2. Тест 2 - проверка ввода количественных значений (положительная)
 - Действия: пользователь вводит целое число > 0
 - Ожидаемый результат: программа запрашивает следующее число

3. Тест 3 - проверка ввода количественных значений (отрицательная)
 - Действия: пользователь вводит не число, нецелое число или целое число <= 0
 - Ожидаемый результат: программа выводит сообщение об ошибке и запрашивает данные еще раз
 
4. Тест 4 - проверка игры двух пользователей
  - Действия: пользователь вводит "20", "2", "Alice", "Bob", затем отвечает "n" и "y" на вопросы о забирании баллов
  - Ожидаемый результат: программа сообщает, какой выиграл пользователь с каким количеством очков

5. Тест 5 - игры с компьютером
  - Действия: пользователь вводит "20", "1", "Alice", "n", "y", затем отвечает "n" и "y" на вопросы о забирании баллов
  - Ожидаемый результат: программа запускает игру с компьютером, по завершении которой сообщает, какой выиграл пользователь с каким количеством очков