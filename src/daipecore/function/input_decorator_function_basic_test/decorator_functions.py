from daipecore.function.input_decorator_function import input_decorator_function
from injecta.container.ContainerInterface import ContainerInterface


@input_decorator_function
def test_input_function():
    def wrapper(container: ContainerInterface):
        return 155

    return wrapper
