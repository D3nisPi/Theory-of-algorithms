from PySide6.QtWidgets import QTreeWidget
from src.lab2.gui.museum_tree_widget_item import MuseumTreeWidgetItem


class MuseumTreeWidget(QTreeWidget):
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        item = self.itemAt(e.pos())
        if isinstance(item, MuseumTreeWidgetItem):
            item.mouse_press_event(e, self.__main_window)
