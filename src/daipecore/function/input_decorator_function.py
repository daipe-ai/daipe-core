from functools import wraps
from daipecore.decorator.ContainerManager import ContainerManager
from daipecore.function import arguments_transformer


def input_decorator_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def executor():
            container = ContainerManager.get_container()

            transformed_args = tuple(arguments_transformer.transform(arg, container) for arg in args)

            return func(*transformed_args, **kwargs)

        return executor

    return wrapper
