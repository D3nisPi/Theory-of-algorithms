from src.lab2.museum.virtual_museum_object import VirtualMuseumObject


class Article(VirtualMuseumObject):
    def __init__(self, object_id: int, title: str, descr: str, views: int, text: str) -> None:
        super().__init__(object_id, title, descr, views)
        self.__text = text

    def __str__(self) -> str:
        return f"Article #{self.id} '{self.title}'. Views: {self.views}"

    def __repr__(self) -> str:
        return (f"Article(id={self.id}, "
                f"title={self.title}, "
                f"descr={self.descr[:31] + '...' if len(self.descr) > 30 else self.descr}, "
                f"text={self.text[:31] + '...' if len(self.text) > 30 else self.text}, "
                f"views={self.views})")

    @property
    def text(self) -> str:
        return self.__text
