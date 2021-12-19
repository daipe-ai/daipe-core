from daipecore.decorator.ContainerManager import ContainerManager
from daipecore.function import arguments_transformer


def input_decorator_function(func):
    def wrapper(*args, **kwargs):
        if func.__module__ != "__main__":
            return None

        container = ContainerManager.get_container()

        transformed_args = tuple(arguments_transformer.transform(arg, container) for arg in args)

        return func(*transformed_args, **kwargs)

    return wrapper
