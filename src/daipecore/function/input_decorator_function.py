from functools import wraps
from daipecore.decorator.ContainerManager import ContainerManager
from daipecore.function import arguments_transformer


def input_decorator_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = ContainerManager.get_container().get_parameters()

        transformed_args = tuple(arguments_transformer.transform(arg, parameters) for arg in args)

        return func(*transformed_args, **kwargs)

    return wrapper
