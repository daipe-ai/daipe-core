from abc import ABC, abstractmethod


class Widgets(ABC):
    @abstractmethod
    def add_text(self, name: str, default_value: str = "", label: str = None):
        pass

    @abstractmethod
    def add_select(self, name: str, choices: list, default_value: str, label: str = None):
        pass

    @abstractmethod
    def add_multiselect(self, name: str, choices: list, default_values: list, label: str = None):
        pass

    @abstractmethod
    def get_value(self, name: str):
        pass

    @abstractmethod
    def remove(self, name: str):
        pass

    @abstractmethod
    def remove_all(self):
        pass

    @abstractmethod
    def should_be_resolved(self) -> bool:
        pass
