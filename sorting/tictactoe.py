# Tic Tac Toe Board


class Solution:
    def hasWin(self, board):
        """
        X if X wins, O if O wins, "Invalid" if both win
        """
        # [] -> [], [X], [O], [X, O]
        # check for Os,
        # check each Row
        wins = set()
        for row in board:
            if row == "OOO":
                wins.add("O")
            if row == "XXX":
                wins.add("X")
        for col in range(3):
            if board[0][col] == "O" and board[1][col] == "O" and board[2][col] == "O":
                wins.add("O")
            if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == "X":
                wins.add("X")
            if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                wins.add("O")
            if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                wins.add("X")
        return wins
# class Solution:
#     def hasWin(self, board):
#         """
#         [] -> [], [X], [O], [X, O]
#         """
#         wins = set()
#         # Check for Os
#         # Check each Row
#         for row in board:
#             if row == "OOO":
#                 wins.add("O")
#             if row == "XXX":
#                 wins.add("X")
#         for col in range(3):
#             if board[0][col] == "O" and board[1][col] == "O" and board[2][col] == "O":
#                 wins.add("O")
#             if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == "X":
#                 wins.add("X")
#         if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
#             wins.add("O")
#         if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
#             wins.add("X")
#         if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
#             wins.add("O")
#         if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
#             wins.add("X")
#         return list(wins)
#     def validTicTacToe(self, board):
#         num_Os = 0
#         for row in board:
#             num_Os += row.count("O")
#         num_Xs = 0
#         for row in board:
#             num_Xs += row.count("X")
#         # Total Xs == Os or Xs == Os + 1
#         if num_Xs != num_Os and num_Xs != num_Os + 1:
#             return False
#         wins = self.hasWin(board)
#         if len(wins) == 2:
#             return False
#         # If there is a win
#         if len(wins) > 0:
#             # If O has won...
#             if "O" in wins:
#                 # Os == Xs
#                 if num_Os != num_Xs:
#                     return False
#             # If X has won
#             if "X" in wins:
#                 # Xs == Os + 1
#                 if num_Xs != num_Os + 1:
#                     return False
#         # Check for all filled squares
#         return True
