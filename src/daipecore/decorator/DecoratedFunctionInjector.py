import types
from daipecore.decorator.BaseDecorator import BaseDecorator


class DecoratedFunctionInjector(type):
    def __call__(cls, *args, **kwargs):
        func = kwargs.pop("func")

        obj: BaseDecorator = cls.__new__(cls, *args, **kwargs)

        if isinstance(func, types.FunctionType):
            obj.set_function(func)
            obj.set_previous_decorator_instance(None)
        else:
            obj.set_function(func._function)
            obj.set_previous_decorator_instance(func)

        obj.__init__(*args, **kwargs)

        return obj
