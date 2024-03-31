"""
This class is responsible for storing all the info about the current state of a chess game
& responsible for determining the valid moves at the current state, this will also keep the move log.
"""

class GameState():
    def __init__(self):
        # board is 8x8 2D list, each element of the list has
        # 2 characters. The 1st character represents the color
        # of the piece, "b" or "w" (black & white)
        # the 2nd character represents the chess piece
        # "--" represents the empty space with no piece on it.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []

