from daipecore.function.input_decorator_function import input_decorator_function
from injecta.container.ContainerInterface import ContainerInterface


@input_decorator_function
def test_input_function1():
    def wrapper(container: ContainerInterface):
        raise Exception("Method must not be called when load_data() is imported to some other notebook as module function")

    return wrapper


@input_decorator_function
def test_input_function2(input_value: int):
    def wrapper(container: ContainerInterface):
        raise Exception("Method must not be called when load_data() is imported to some other notebook as module function")

    return wrapper
