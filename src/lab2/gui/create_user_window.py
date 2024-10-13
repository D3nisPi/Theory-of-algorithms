from PySide6.QtCore import QSize, QMargins
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, \
    QMessageBox
import src.lab2.client as client
import src.lab2.gui.login_window as login
from src.lab2.gui.main_window import MainWindow
from src.lab2.museum.user import User


class CreateUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__login_window = None
        self.setWindowTitle("Создание нового пользователя")
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

        name_label = QLabel("Имя")
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        name_label.setFont(QFont("Arial", 16))
        name_label.setFixedSize(QSize(100, 50))

        name_text = QLineEdit()
        name_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        name_text.setFont(QFont("Arial", 16))
        name_text.setFixedSize(QSize(200, 50))

        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_text)

        create_button = QPushButton("Создать")
        create_button.setStyleSheet("font-family: Arial; font-size: 13pt;")
        create_button.setFixedSize(QSize(100, 50))
        create_button.setContentsMargins(QMargins(0, 0, 0, 0))
        create_button.clicked.connect(self.__on_create_clicked)

        exit_button = QPushButton("Назад")
        exit_button.setStyleSheet("font-family: Arial; font-size: 13pt;")
        exit_button.setFixedSize(QSize(100, 50))
        exit_button.setContentsMargins(QMargins(0, 0, 0, 0))
        exit_button.clicked.connect(self.__on_exit_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(create_button)
        button_layout.addWidget(exit_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(id_layout)
        main_layout.addLayout(name_layout)
        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.__id_text = id_text
        self.__name_text = name_text

    def __on_exit_clicked(self):
        self.__login_window = login.LogInWindow()
        self.__login_window.show()
        self.close()

    def __on_create_clicked(self):
        if not self.__id_text.text().lstrip('-').isdecimal():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите корректное число")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            return

        user_id = int(self.__id_text.text())
        name = self.__name_text.text()
        try:
            client.add_user(user_id, name)
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText(f"Ошибка: {e}")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            return

        self.__window = MainWindow(User(user_id, name))
        self.__window.show()
        self.close()
