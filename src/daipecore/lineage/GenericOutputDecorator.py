from daipecore.lineage.OutputDecoratorInterface import OutputDecoratorInterface


class GenericOutputDecorator(OutputDecoratorInterface):
    def __init__(self, identifier: str):
        self.__identifier = identifier

    @property
    def identifier(self):
        return self.__identifier
