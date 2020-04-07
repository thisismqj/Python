import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QWidget()
	win.resize(320, 240)
	win.setWindowTitle("WTFuckingQT")
	win.show()
	sys.exit(app.exec_())
