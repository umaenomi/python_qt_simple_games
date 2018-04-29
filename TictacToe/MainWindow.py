import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pui.main_form_ui import Ui_MainWindow
from PlayerDialog import ConfigurationDialog
from TicTacToeWidget import Player


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew_Game.triggered.connect(self.start_new_game)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.gameBoard.current_player_changed[Player].connect(self.update_name_labels)
        self.ui.gameBoard.game_over[Player].connect(self.handle_game_over)
        self.start_new_game()
        self.show()

    def start_new_game(self):
        dlg = ConfigurationDialog()
        if not dlg.exec_():
            return
        self.set_label_font()
        self.ui.player1.setText(dlg.player1_name())
        self.ui.player2.setText(dlg.player2_name())
        self.ui.gameBoard.init_new_game()
        self.ui.gameBoard.setEnabled(True)

    def update_name_labels(self):
        font = self.ui.player1.font()
        font.setBold(self.ui.gameBoard.current_player() == Player.Player1)
        self.ui.player1.setFont(font)
        font.setBold(self.ui.gameBoard.current_player() == Player.Player2)
        self.ui.player2.setFont(font)

    def handle_game_over(self, winner):
        self.ui.gameBoard.setEnabled(False)
        if winner == Player.Draw:
            message = "Игра завершилась вничью"
        else:
            message = "{} выиграл".format(self.ui.player1.text() if winner == Player.Player1 else self.ui.player2.text())
        QMessageBox.information(self, "Результат игры", message)

    def set_label_font(self):
        font = self.ui.player1.font()
        font.setBold(True)
        self.ui.player1.setFont(font)
        font.setBold(False)
        self.ui.player2.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MainWindow()
    sys.exit(app.exec_())
