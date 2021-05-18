from abc import ABC, abstractmethod


class OutputDecoratorInterface(ABC):
    @property
    @abstractmethod
    def identifier(self):
        pass
