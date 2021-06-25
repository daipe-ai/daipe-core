from abc import ABC, abstractmethod


class Widgets(ABC):
    @abstractmethod
    def add_text(self, name: str, default_value: str, label: str = None):
        pass

    @abstractmethod
    def add_select(self, name: str, choices: list, label: str = None):
        pass

    @abstractmethod
    def add_multiselect(self, name: str, choices: list, label: str = None):
        pass

    @abstractmethod
    def get_value(self, name: str):
        pass

    @abstractmethod
    def should_be_resolved(self) -> bool:
        pass
