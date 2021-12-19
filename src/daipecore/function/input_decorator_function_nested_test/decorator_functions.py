from daipecore.function.input_decorator_function import input_decorator_function
from injecta.container.ContainerInterface import ContainerInterface


@input_decorator_function
def test_input_function1():
    def wrapper(container: ContainerInterface):
        return 140

    return wrapper


@input_decorator_function
def test_input_function2(input_value: int):
    def wrapper(container: ContainerInterface):
        return input_value + 5

    return wrapper


@input_decorator_function
def test_input_function3(input_value: int):
    def wrapper(container: ContainerInterface):
        return input_value + 10

    return wrapper
