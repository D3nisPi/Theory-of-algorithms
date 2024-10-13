from abc import ABC, abstractmethod


class ViewableMixin(ABC):
    @property
    @abstractmethod
    def views(self) -> int:
        pass

    @abstractmethod
    def view(self) -> None:
        pass
