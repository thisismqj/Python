import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QWidget()
	win.setGeometry(128, 128, 256, 256)
	win.setWindowTitle('The QT test!')
	label = QLabel(win)
	label.setText('Hello, World!')
	label.move(50, 50)
	win.show()
	sys.exit(app.exec_())

