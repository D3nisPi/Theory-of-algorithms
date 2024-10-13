from PySide6.QtCore import QSize, QMargins
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, \
    QMessageBox
import src.lab2.client as client
from src.lab2.gui.create_user_window import CreateUserWindow
from src.lab2.gui.main_window import MainWindow
from src.lab2.museum.user import User


class LogInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.setWindowTitle("Вход")
        self.setFixedSize(QSize(360, 200))

        id_label = QLabel("Id")
        id_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        id_label.setFont(QFont("Arial", 16))
        id_label.setFixedSize(QSize(100, 50))

        id_text = QLineEdit()
        id_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        id_text.setFont(QFont("Arial", 16))
        id_text.setFixedSize(QSize(200, 50))

        id_layout = QHBoxLayout()
        id_layout.addWidget(id_label)
        id_layout.addWidget(id_text)

        create_button = QPushButton("Создать")
        create_button.setStyleSheet("font-family: Arial; font-size: 13pt;")
        create_button.setFixedSize(QSize(100, 50))
        create_button.setContentsMargins(QMargins(0, 0, 0, 0))
        create_button.clicked.connect(self.__on_create_clicked)

        exit_button = QPushButton("Выйти")
        exit_button.setStyleSheet("font-family: Arial; font-size: 13pt;")
        exit_button.setFixedSize(QSize(100, 50))
        exit_button.setContentsMargins(QMargins(0, 0, 0, 0))
        exit_button.clicked.connect(self.__on_exit_clicked)

        login_button = QPushButton("Войти")
        login_button.setStyleSheet("font-family: Arial; font-size: 13pt;")
        login_button.setFixedSize(QSize(100, 50))
        login_button.setContentsMargins(QMargins(0, 0, 0, 0))
        login_button.clicked.connect(self.__on_login_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(create_button)
        button_layout.addWidget(exit_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(id_layout)
        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.__id_text = id_text

    def __on_exit_clicked(self):
        self.close()

    def __on_create_clicked(self):
        self.__window = CreateUserWindow()
        self.__window.show()
        self.close()

    def __on_login_clicked(self):
        if not self.__id_text.text().lstrip('-').isdecimal():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите корректное число")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            return

        user_id = int(self.__id_text.text())
        try:
            name = client.get_user_name(user_id)
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText(f"Ошибка: {e}")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            return

        if name is None:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Пользователь с данным id не зарегестрирован")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            return

        self.__window = MainWindow(User(user_id, name))
        self.__window.show()
        self.close()
