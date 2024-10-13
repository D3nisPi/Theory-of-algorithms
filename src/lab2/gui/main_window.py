from PySide6.QtCore import QSize, QMargins
from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton, QMessageBox
from src.lab2.gui.museum_tree_widget import MuseumTreeWidget
from src.lab2.gui.museum_tree_widget_item import MuseumTreeWidgetItem
import src.lab2.client as client
import src.lab2.gui.login_window as login
from src.lab2.museum.thematic_collection import ThematicCollection
from src.lab2.museum.user import User
from src.lab2.museum.virtual_museum import VirtualMuseum
from src.lab2.reports.excel_report_maker import ExcelReportMaker
from src.lab2.reports.word_report_maker import WordReportMaker


class MainWindow(QMainWindow):
    def __init__(self, user: User):
        super().__init__()
        self.__login_window = None
        self.__museum = VirtualMuseum(user)

        self.setWindowTitle("Виртуальный музей")
        self.setFixedSize(QSize(1600, 900))

        tree = MuseumTreeWidget(self)
        tree.setHeaderLabel("Музей")
        tree.setFixedSize(QSize(400, 900))
        tree.setFont(QFont("Arial", 16))
        tree.setContentsMargins(QMargins(0, 0, 0, 0))
        self.init_tree(tree)

        title = QLabel("")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        title.setFont(QFont("Arial", 16))
        title.setFixedSize(QSize(800, 100))
        title.setContentsMargins(QMargins(0, 0, 0, 0))
        title.setWordWrap(True)

        views = QLabel("")
        views.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        views.setFont(QFont("Arial", 16))
        views.setFixedSize(QSize(200, 100))
        views.setContentsMargins(QMargins(0, 0, 0, 0))
        views.setWordWrap(True)

        view_header_layout = QHBoxLayout()
        view_header_layout.addWidget(title)
        view_header_layout.addWidget(views)
        view_header_layout.setContentsMargins(QMargins(0, 0, 0, 0))

        data = QLabel("")
        data.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        data.setFont(QFont("Arial", 16))
        data.setWordWrap(True)
        data.setFixedSize(QSize(1000, 600))
        data.setContentsMargins(QMargins(0, 0, 0, 0))

        description = QLabel("")
        description.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        description.setFont(QFont("Arial", 16))
        description.setFixedSize(QSize(1000, 200))
        description.setContentsMargins(QMargins(0, 0, 0, 0))
        description.setWordWrap(True)

        view_layout = QVBoxLayout()
        view_layout.addLayout(view_header_layout)
        view_layout.addWidget(data)
        view_layout.addWidget(description)
        view_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        view_layout.setSpacing(0)

        user_header = QLabel("Информация о пользователе")
        user_header.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        user_header.setFont(QFont("Arial", 16))
        user_header.setFixedSize(QSize(200, 100))
        user_header.setContentsMargins(QMargins(0, 0, 0, 0))
        user_header.setWordWrap(True)

        user_id = QLabel(f"Id пользователя: {self.__museum.user.id}")
        user_id.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        user_id.setFont(QFont("Arial", 16))
        user_id.setFixedSize(QSize(200, 100))
        user_id.setContentsMargins(QMargins(0, 0, 0, 0))
        user_id.setWordWrap(True)

        username = QLabel(f"Имя пользователя: {self.__museum.user.name}")
        username.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        username.setFont(QFont("Arial", 16))
        username.setFixedSize(QSize(200, 100))
        username.setContentsMargins(QMargins(0, 0, 0, 0))
        username.setWordWrap(True)

        exit_button = QPushButton("Выйти")
        exit_button.setStyleSheet("font-family: Arial; font-size: 16pt;")
        exit_button.setFixedSize(QSize(200, 100))
        exit_button.setContentsMargins(QMargins(0, 0, 0, 0))
        exit_button.clicked.connect(self.__on_exit_clicked)

        user_info_layout = QVBoxLayout()
        user_info_layout.addWidget(user_header)
        user_info_layout.addWidget(user_id)
        user_info_layout.addWidget(username)
        user_info_layout.addWidget(exit_button)
        user_info_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        user_info_layout.setSpacing(0)

        report_header = QLabel("Отчеты")
        report_header.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        report_header.setFont(QFont("Arial", 16))
        report_header.setFixedSize(QSize(200, 100))
        report_header.setContentsMargins(QMargins(0, 0, 0, 0))

        report_word = QPushButton("Word")
        report_word.setStyleSheet("font-family: Arial; font-size: 16pt;")
        report_word.setFixedSize(QSize(200, 100))
        report_word.setContentsMargins(QMargins(0, 0, 0, 0))
        report_word.clicked.connect(self.__on_word_report_clicked)

        report_excel = QPushButton("Excel")
        report_excel.setStyleSheet("font-family: Arial; font-size: 16pt;")
        report_excel.setFixedSize(QSize(200, 100))
        report_excel.setContentsMargins(QMargins(0, 0, 0, 0))
        report_excel.clicked.connect(self.__on_excel_report_clicked)

        report_layout = QVBoxLayout()
        report_layout.addWidget(report_header)
        report_layout.addWidget(report_word)
        report_layout.addWidget(report_excel)
        report_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        report_layout.setSpacing(0)

        free_space = QWidget()
        free_space.setFixedSize(QSize(200, 200))
        free_space.setContentsMargins(QMargins(0, 0, 0, 0))

        right_layout = QVBoxLayout()
        right_layout.addLayout(user_info_layout)
        right_layout.addWidget(free_space)
        right_layout.addLayout(report_layout)
        right_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        right_layout.setSpacing(0)

        main_layout = QHBoxLayout()
        main_layout.addWidget(tree)
        main_layout.addLayout(view_layout)
        main_layout.addLayout(right_layout)
        main_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        main_layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.title = title
        self.views = views
        self.data = data
        self.description = description

    @property
    def museum(self):
        return self.__museum

    def __on_exit_clicked(self, e):
        self.__login_window = login.LogInWindow()
        self.__login_window.show()
        self.close()

    def __on_word_report_clicked(self, e):
        report = WordReportMaker(self.__museum)
        report.make()

    def __on_excel_report_clicked(self, e):
        report = ExcelReportMaker(self.__museum)
        report.make()

    def init_tree(self, tree):
        try:
            collections = client.get_collection_data(0)
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText(f"Ошибка: {e}")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.__login_window = login.LogInWindow()
            self.__login_window.show()
            self.close()
            return

        for collection in collections:
            if isinstance(collection, ThematicCollection):
                self.__museum.append(collection)

        nodes = [MuseumTreeWidgetItem(collection) for collection in collections]
        tree.addTopLevelItems(nodes)
