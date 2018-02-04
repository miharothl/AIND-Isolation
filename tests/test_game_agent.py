"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""
import timeit
import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"
        self.fail("Hello, World!")


    def test_minimax(self):

        TIME_LIMIT_MILLIS = 3600000

        time_millis = lambda: 1000 * timeit.default_timer()

        move_start = time_millis()
        time_left = lambda : TIME_LIMIT_MILLIS - (time_millis() - move_start)

        minimax_player = game_agent.MinimaxPlayer()

        game = isolation.Board(minimax_player, self.player2)

        legal_moves = game.get_legal_moves()

        acitve_p = game.active_player

        legal_moves_2 = game.get_legal_moves(player=acitve_p)

        minimax_move = minimax_player.get_move(game, time_left)
        # minimax_move = minimax_player.minimax_decision(self.game, 3, 0)

    def test_game(self):

        # place player 1 on the board at row 2, column 3, then place player 2 on
        # the board at row 0, column 5; display the resulting board state.  Note
        # that the .apply_move() method changes the calling object in-place.
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

        # players take turns moving on the board, so player1 should be next to move
        assert(self.player1 == self.game.active_player)

        # get a list of the legal moves available to the active player
        print(self.game.get_legal_moves())

        # get a successor of the current state by making a copy of the board and
        # applying a move. Notice that this does NOT change the calling object
        # (unlike .apply_move()).
        new_game = self.game.forecast_move((1, 1))
        assert(new_game.to_string() != self.game.to_string())
        print("\nOld state:\n{}".format(self.game.to_string()))
        print("\nNew state:\n{}".format(new_game.to_string()))



        # best_moves = set([(0, 0), (2, 0), (0, 1)])
        # rootNode = game.GameState()
        # minimax_move = minimax.minimax_decision(rootNode)
        #
        # print("Best move choices: {}".format(list(best_moves)))
        # print("Your code chose: {}".format(minimax_move))
        #
        # if minimax_move in best_moves:
        #     print("That's one of the best move choices. Looks like your minimax-decision function worked!")
        # else:
        #     print("Uh oh...looks like there may be a problem.")


if __name__ == '__main__':
    unittest.main()
