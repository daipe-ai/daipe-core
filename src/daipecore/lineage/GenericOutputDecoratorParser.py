import _ast
from daipecore.lineage.DecoratorParserInterface import DecoratorParserInterface
from daipecore.lineage.GenericOutputDecorator import GenericOutputDecorator


class GenericOutputDecoratorParser(DecoratorParserInterface):
    def __init__(self, name: str):
        self.__name = name

    def parse(self, decorator: _ast.Call):
        arg: _ast.Str = decorator.args[0]

        return GenericOutputDecorator(arg.s)

    def get_name(self) -> str:
        return self.__name
