import _ast
from abc import ABC, abstractmethod


class DecoratorParserInterface(ABC):
    @abstractmethod
    def parse(self, decorator: _ast.Call):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
