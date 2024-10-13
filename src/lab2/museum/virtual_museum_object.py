from abc import ABC, abstractmethod
from src.lab2.museum.viewable_mixin import ViewableMixin


class VirtualMuseumObject(ViewableMixin, ABC):
    def __init__(self, object_id: int, title: str, descr: str, views: int) -> None:
        self.__id = object_id
        self.__title = title
        self.__descr = descr
        self.__views = views

    def __hash__(self) -> int:
        return hash(self.__id)

    def __eq__(self, other) -> bool:
        if not isinstance(other, VirtualMuseumObject):
            raise TypeError(f"Unsupported operand type(s) for ==: 'VirtualMuseumObject' and '{type(other)}'")
        return self.__id == other.__id

    def __ne__(self, other) -> bool:
        if not isinstance(other, VirtualMuseumObject):
            raise TypeError(f"Unsupported operand type(s) for !=: 'VirtualMuseumObject' and '{type(other)}'")
        return self.__id != other.__id

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @property
    def title(self) -> str:
        return self.__title

    @property
    def descr(self) -> str:
        return self.__descr

    @property
    def id(self) -> int:
        return self.__id

    @property
    def views(self) -> int:
        return self.__views

    def view(self) -> None:
        self.__views += 1
