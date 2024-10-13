import sys
from PySide6.QtWidgets import QApplication
from src.lab2.gui.login_window import LogInWindow


def main():
    app = QApplication(sys.argv)
    window = LogInWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()