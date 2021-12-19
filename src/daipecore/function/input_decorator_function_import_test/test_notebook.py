import os
from daipecore.decorator.notebook_function import notebook_function
from daipecore.function.input_decorator_function_import_test.decorator_functions import test_input_function2, test_input_function1

os.environ["APP_ENV"] = "test"


@notebook_function(test_input_function2(test_input_function1()))
def load_data(input_value):
    return input_value + 10
