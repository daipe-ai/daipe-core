from daipecore.lineage.argument.DecoratorInputFunctionInterface import DecoratorInputFunctionInterface


class FunctionCallAttribute:
    def __init__(self, function: DecoratorInputFunctionInterface, attribute_name: str):
        self.__function = function
        self.__attribute_name = attribute_name

    @property
    def function(self):
        return self.__function

    @property
    def attribute_name(self):
        return self.__attribute_name
