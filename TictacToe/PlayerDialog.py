import sys
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox
from pui.player_dialog_ui import Ui_Dialog


class ConfigurationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.update_ok_button_state()
        self.show()

    def update_ok_button_state(self):
        pl1_text = self.ui.player1_name.text()
        pl1_name_empty = not(pl1_text and pl1_text.strip())
        pl2_text = self.ui.player2_name.text()
        pl2_name_empty = not(pl2_text and pl2_text.strip())
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        ok_button.setDisabled(pl1_name_empty or pl2_name_empty)

    def set_player1_name(p1name):
        self.ui.player2_name.setText(p1name)

    def set_player2_name(p2name):
        self.ui.player2_name.setText(p1name)

    def player1_name(self):
        return self.ui.player1_name.text()

    def player2_name(self):
        return self.ui.player2_name.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ConfigurationDialog()
    sys.exit(app.exec_())
