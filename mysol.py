class Game:
    def __init__(self):
        self.board = Game.Board()
        self.player1 = Game.Player("Sanji", "x")
        self.player2 = Game.Player("Joe", "o")

    class Board:
        def __init__(self):
            self.board = [[" " for _ in range(3)] for _ in range(3)]

        def make_move(self, mark, move):
            self.board[move[0]][move[1]] = mark

        def is_full(self):
            return all(cell != " " for row in self.board for cell in row)

        def check_winner(self, player):
            for i in range(3):
                if all(self.board[i][j] == player for j in range(3)) or all(
                        self.board[j][i] == player for j in range(3)):
                    return True
            if all(self.board[i][i] == player for i in range(3)) or all(
                    self.board[i][2 - i] == player for i in range(3)):
                return True
            return False

        def __str__(self):
            return ("-------------\n"
                    f"| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |\n"
                    "|-----------|\n"
                    f"| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |\n"
                    "|-----------|\n"
                    f"| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |\n"
                    "-------------")

    class Player:
        def __init__(self, name, mark):
            self.name = name
            self.mark = mark
            self.score = 0


def main():
    game = Game()

    # while !board.is_full() && :

    game.board.make_move(game.player1.mark, [1, 1])
    print(game.board)
    game.board.make_move(game.player2.mark, [0, 0])
    print(game.board)


main()
