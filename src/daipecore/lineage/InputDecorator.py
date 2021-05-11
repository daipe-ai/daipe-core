from daipecore.lineage.InputDecoratorInterface import InputDecoratorInterface


class InputDecorator(InputDecoratorInterface):
    def __init__(self, name, args):
        self.__name = name
        self.__args = args

    @property
    def name(self):
        return self.__name

    @property
    def args(self):
        return self.__args
