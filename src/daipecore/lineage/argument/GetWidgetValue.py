from daipecore.lineage.argument.DecoratorInputFunctionInterface import DecoratorInputFunctionInterface


class GetWidgetValue(DecoratorInputFunctionInterface):
    def __init__(self, name: str):
        self.__name = name

    @property
    def identifier(self):
        return self.__name
