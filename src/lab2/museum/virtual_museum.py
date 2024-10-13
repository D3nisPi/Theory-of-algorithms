from collections.abc import Sequence
from typing import List
from src.lab2.museum.thematic_collection import ThematicCollection
from src.lab2.museum.user import User


class VirtualMuseum(Sequence):
    def __init__(self, user: User = None, collections: List[ThematicCollection] = None) -> None:
        self.__collections = collections or []
        self.__user = user

    def __getitem__(self, index: int) -> ThematicCollection:
        if index < 0 or index >= len(self.__collections):
            raise IndexError("Index is out of range")
        return self.__collections[index]

    def __len__(self) -> int:
        return len(self.__collections)

    @property
    def user(self) -> User | None:
        return self.__user

    @user.setter
    def user(self, user) -> None:
        self.__user = user

    def append(self, collection: ThematicCollection) -> None:
        self.__collections.append(collection)
