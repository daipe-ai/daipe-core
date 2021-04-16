from abc import ABC, abstractmethod


class ArgumentMappingInterface(ABC):
    @abstractmethod
    def get_mapping(self) -> dict:
        pass
