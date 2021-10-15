from injecta.container.ContainerInterface import ContainerInterface
from daipecore.decorator.BaseDecorator import BaseDecorator
from daipecore.decorator.DecoratedFunctionInjector import DecoratedFunctionInjector
from daipecore.function.ArgumentsResolver import ArgumentsResolver
from daipecore.function.function_inspector import inspect_function


class InputDecorator(BaseDecorator, metaclass=DecoratedFunctionInjector):
    _immediate_execution_enabled = True
    _result = None

    @staticmethod
    def enable_immediate_execution():
        InputDecorator._immediate_execution_enabled = True

    @staticmethod
    def disable_immediate_execution():
        InputDecorator._immediate_execution_enabled = False

    def set_result(self, result):
        self._result = result

    @property
    def immediate_execution_enabled(self):
        return InputDecorator._immediate_execution_enabled

    @property
    def result(self):
        return self._result

    def prepare_arguments(self, container: ContainerInterface):
        arguments_resolver: ArgumentsResolver = container.get(ArgumentsResolver)
        return arguments_resolver.resolve(inspect_function(self._function), self._args)

    def after_execution(self, container: ContainerInterface):
        pass
