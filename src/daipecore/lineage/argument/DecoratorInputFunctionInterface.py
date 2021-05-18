from abc import ABC, abstractmethod


class DecoratorInputFunctionInterface(ABC):
    @property
    @abstractmethod
    def identifier(self):
        pass
