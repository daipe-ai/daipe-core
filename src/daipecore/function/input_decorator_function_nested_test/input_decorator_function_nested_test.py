import os
from daipecore.decorator.notebook_function import notebook_function
from daipecore.function.input_decorator_function_nested_test.decorator_functions import (
    test_input_function3,
    test_input_function2,
    test_input_function1,
)

os.environ["APP_ENV"] = "test"


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
