import os
from daipecore.decorator.notebook_function import notebook_function
from daipecore.function.input_decorator_function import input_decorator_function
from injecta.container.ContainerInterface import ContainerInterface

os.environ["APP_ENV"] = "test"


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


@notebook_function(test_input_function3(test_input_function2(test_input_function1())))
def load_data(input_value):
    return input_value


@notebook_function(load_data)
def rename_columns(police_number: int):
    assert police_number == 155


if __name__ == "__main__":
    assert isinstance(load_data, notebook_function)
    assert load_data.result == 155
    assert isinstance(rename_columns, notebook_function)
    assert rename_columns.result is None
