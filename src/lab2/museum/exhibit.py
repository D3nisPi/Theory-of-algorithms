from src.lab2.museum.virtual_museum_object import VirtualMuseumObject


class Exhibit(VirtualMuseumObject):
    def __init__(self, object_id: int, title: str, descr: str, views: int, image_data: bytes) -> None:
        super().__init__(object_id, title, descr, views)
        self.__image_data = image_data

    def __str__(self) -> str:
        return f"Exhibit #{self.id} '{self.title}'. Views: {self.views}"

    def __repr__(self) -> str:
        return (f"Exhibit(id={self.id}, "
                f"title={self.title}, "
                f"descr={self.descr[:31] + '...' if len(self.descr) > 30 else self.descr}, "
                f"views={self.views})")

    @property
    def image_data(self) -> bytes:
        return self.__image_data
