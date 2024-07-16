# model.py
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, x, y):
        if self.board[x][y] == ' ':
            self.board[x][y] = self.current_player
            if self.check_winner():
                return f'Player {self.current_player} wins!'
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            return 'Invalid move!'

    def check_winner(self):
        # Проверка горизонталей, вертикалей и диагоналей на наличие победителя
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

# view.py
class ConsoleView:
    @staticmethod
    def display_board(board):
        for row in board:
            print('|'.join(row))
            print('-' * 5)

    @staticmethod
    def get_move():
        x = int(input("Enter row (0, 1, 2): "))
        y = int(input("Enter column (0, 1, 2): "))
        return x, y

# controller.py
class GameController:
    def __init__(self, game, view):
        self.game = game
        self.view = view

    def play(self):
        while True:
            self.view.display_board(self.game.board)
            x, y = self.view.get_move()
            result = self.game.make_move(x, y)
            if result:
                self.view.display_board(self.game.board)
                print(result)
                break

# main.py
if __name__ == "__main__":
    from model import Game
    from view import ConsoleView
    from controller import GameController

    game = Game()
    view = ConsoleView()
    controller = GameController(game, view)
    controller.play()
