class FunctionLink:
    def __init__(self, linked_function):
        self.__linked_function = linked_function

    @property
    def linked_function(self):
        return self.__linked_function
