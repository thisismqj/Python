import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle('My Form')
        self.edit = QLineEdit("Enter your password:")
        self.button = QPushButton("Bomb!")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greeting)
    def greeting(self):
        print('Hello, {}'.format(self.edit.text()))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())