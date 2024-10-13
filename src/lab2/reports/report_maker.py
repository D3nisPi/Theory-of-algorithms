from abc import ABC, abstractmethod


class ReportMaker(ABC):
    def __init__(self, museum) -> None:
        self._museum = museum

    @abstractmethod
    def make(self, path: str = None) -> None:
        pass
