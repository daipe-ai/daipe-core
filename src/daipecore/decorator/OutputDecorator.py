from injecta.container.ContainerInterface import ContainerInterface
from daipecore.decorator.BaseDecorator import BaseDecorator
from daipecore.decorator.DecoratedFunctionInjector import DecoratedFunctionInjector


class OutputDecorator(BaseDecorator, metaclass=DecoratedFunctionInjector):
    def modify_result(self, result, container: ContainerInterface):
        return result

    def process_result(self, result, container: ContainerInterface):
        pass
