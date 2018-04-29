import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import QSignalMapper, pyqtSignal, QObject
from enum import Enum

class Player(Enum):
    Invalid = 0,
    Player1 = 1,
    Player2 = 2,
    Draw = 3


class TictactoeWidget(QWidget):
    current_player_changed = pyqtSignal(Player, name='current_player_changed')
    game_over = pyqtSignal(Player, name='game_over')

    def __init__(self, arg):
        super().__init__()
        self.board = []
        self.cur_player = Player.Player1
        self.initUI()
        
    def initUI(self):
        self.setup_board()
        self.show()

    def setup_board(self):
        gridLayout = QGridLayout()
        mapper = QSignalMapper(self)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                button.setText(" ")
                gridLayout.addWidget(button, row, column)
                self.board.append(button)
                mapper.setMapping(button, len(self.board) - 1)
                button.clicked.connect(mapper.map)

        mapper.mapped.connect(self.handle_button_click)
        self.setLayout(gridLayout)

    def init_new_game(self):
        for button in self.board:
            button.setText(" ")
        self.cur_player = Player.Player1

    def handle_button_click(self,index):
        if index < 0 or index > len(self.board):
            return
        button = self.board[index]
        if button.text() != " ":
            return
        text = "X" if self.current_player() == Player.Player1 else "O"
        button.setText(text)
        winner = self.check_win_condition(index // 3, index % 3)
        if winner == Player.Invalid:
            self.set_current_player(Player.Player2 if self.current_player() == Player.Player1 else Player.Player1)
            return
        else:
            self.game_over.emit(winner)


    def current_player(self):
        return self.cur_player


    def set_current_player(self, p):
        if self.cur_player == p:
            return
        self.cur_player = p
        self.current_player_changed.emit(p)


    def check_win_condition(self, row, column):
        current = self.board[row * 3 + column].text()
        count = 0;
        # Проверяем горизонтальные последовательности
        for c in range(3):
            if self.board[row*3+c].text() == current:
                count +=1
        if count == 3:
            return self.current_player()
        count = 0
        # Проверяем вертикальные последовательности
        for r in range(3): 
            if self.board[r*3+column].text() == current:
                count += 1
        if count == 3:
            return self.current_player()
        # Если ход был сделан по диагонали, проверяем диагонали
        count = 0
        if row == column:
            for c in range(3):
                if self.board[c*3+c].text() == current:
                    count += 1
            if count == 3:
                return self.current_player()
        count = 0
        if row + column == 2:
            for c in range(3):
                if self.board[(2-c)*3+c].text() == current:
                    count += 1
            if count == 3:
                return self.current_player()
        # Проверяем осталисть ли свободные ячейки
        for button in self.board:
            if button.text() == " ":
                return Player.Invalid
        return Player.Draw


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TictactoeWidget()
    sys.exit(app.exec_())
