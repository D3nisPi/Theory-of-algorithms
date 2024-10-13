from collections.abc import Sequence
from src.lab2.museum.virtual_museum_object import VirtualMuseumObject
from typing import List


class ThematicCollection(VirtualMuseumObject, Sequence):
    def __init__(self, object_id: int, title: str, descr: str, views: int,
                 items: List[VirtualMuseumObject] = None) -> None:
        super().__init__(object_id, title, descr, views)
        self.__items = items or []
        self.__initialized = items is not None

    def __getitem__(self, index: int) -> VirtualMuseumObject:
        if index < 0 or index >= len(self.__items):
            raise IndexError("Index is out of range")
        return self.__items[index]

    def __len__(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return (f"ThematicCollection #{self.id} '{self.title}'. Views: {self.views}"
                f"({','.join(map(str, self.__items))})")

    def __repr__(self) -> str:
        return (f"ThematicCollection(id={self.id}, "
                f"title={self.title}, "
                f"descr={self.descr[:31] + '...' if len(self.descr) > 30 else self.descr}, "
                f"views={self.views}"
                f"({','.join(map(repr, self.__items))}))")

    @property
    def initialized(self) -> bool:
        return self.__initialized

    def append(self, item: VirtualMuseumObject) -> None:
        self.__initialized = True
        self.__items.append(item)
