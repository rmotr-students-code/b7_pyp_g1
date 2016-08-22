class Player(object):
    def move(self):
        pass


class Board(object):
    pass


class Game(object):
    def move(player)


class Move(object):
    player = 
    position = 
    board = 

iniitial_state = 
moves = [m1, m2, m3]


# ======== User ========

test_game_is_won:
    game = Game()
    game.move(0, 1)
    game.move(0, 2)
    
    game.move(0, 3)
    
    self.assertEqual(game.winner, 'X')


test_game_fails_if_invalid_position:
    game = Game()
    with self.assertRaises(InvalidPositionException):
        game.move(0, 4)
        
ph = Photo()
al = Album()

al.is_present_photo(ph)

photo in album