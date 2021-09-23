import _ast
from daipecore.lineage.DecoratorParserInterface import DecoratorParserInterface
from injecta.module import attribute_loader
from daipecore.lineage.argument.ArgumentParser import ArgumentParser
from daipecore.decorator.utils import get_decorator_id


class InputDecoratorParser(DecoratorParserInterface):
    def __init__(self, name: str, module_name: str, class_name: str, argument_parser: ArgumentParser):
        self.__name = name
        self.__module_name = module_name
        self.__class_name = class_name
        self.__argument_parser = argument_parser

    def parse(self, decorator: _ast.Call):
        args = [self.__argument_parser.parse(arg) for arg in decorator.args]

        class_ = attribute_loader.load(self.__module_name, self.__class_name)

        return class_(get_decorator_id(decorator), args)

    def get_name(self) -> str:
        return self.__name
