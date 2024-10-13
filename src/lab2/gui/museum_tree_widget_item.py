from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox
import src.lab2.client as client
from src.lab2.museum.article import Article
from src.lab2.museum.exhibit import Exhibit
from src.lab2.museum.thematic_collection import ThematicCollection
from src.lab2.museum.virtual_museum_object import VirtualMuseumObject


class MuseumTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, museum_object: VirtualMuseumObject, parent = None):
        super().__init__(parent, [str(museum_object)])
        self.__museum_object = museum_object
        self.setText(0, museum_object.title)

    def mouse_press_event(self, e, window):
        if e.button() == Qt.MouseButton.LeftButton:
            self.__museum_object.view()
            try:
                client.update_user_views(window.museum.user.id, self.__museum_object.id, self.__museum_object.views)
            except Exception as e:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Ошибка")
                msg_box.setText(f"Ошибка: {e}")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.exec()
                return

            if not isinstance(self.__museum_object, ThematicCollection):
                self.__update_window(window)
                return
            if self.__museum_object.initialized:
                self.__update_window(window)
                return

            try:
                collection_data = client.get_collection_data(self.__museum_object.id)
            except Exception as e:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Ошибка")
                msg_box.setText(f"Ошибка: {e}")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.exec()
                return

            for item in collection_data:
                self.__museum_object.append(item)
                self.addChild(MuseumTreeWidgetItem(item, self))

            self.__update_window(window)
            self.setExpanded(True)

    def __update_window(self, window):
        window.title.setText(f"Название: {self.__museum_object.title}")
        window.views.setText(f"Просмотры: {self.__museum_object.views}")
        window.description.setText(f"Описание: {self.__museum_object.descr}")

        if isinstance(self.__museum_object, ThematicCollection):
            lst = '\n\t'.join([item.title for item in self.__museum_object])
            window.data.setText(f"Содержание:\n\t{lst}")
        elif isinstance(self.__museum_object, Article):
            window.data.setText(self.__museum_object.text)
        elif isinstance(self.__museum_object, Exhibit):
            pixmap = QPixmap()
            pixmap.loadFromData(self.__museum_object.image_data)
            scaled_pixmap = pixmap.scaled(window.data.width(), window.data.height(),
                                          aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
            window.data.setPixmap(scaled_pixmap)
