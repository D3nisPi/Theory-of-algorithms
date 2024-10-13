class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.__id = user_id
        self.__name = name

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name})"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name
