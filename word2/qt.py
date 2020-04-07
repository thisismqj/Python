import sys
from PyQt5.QtWidgets import QApplication, QWidget
import gui

if __name__ == '__main__':
    # 创建QApplication
    app = QApplication(sys.argv)
    # 创建窗口
    win = QWidget()
    ui = gui.Ui_Form()
    ui.setupUi(win)
    # 设置大小
    # 移动窗口
    win.move(233, 555)
    # 设置窗口标题
    # 显示窗口
    win.show()
    # 主事件循环
    sys.exit(app.exec())
