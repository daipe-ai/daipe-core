from abc import ABC, abstractmethod


class InputDecoratorInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def args(self):
        pass
