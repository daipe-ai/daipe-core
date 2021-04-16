from injecta.parameter.all_placeholders_replacer import find_all_placeholders, replace_all_placeholders
from daipecore.decorator.ContainerManager import ContainerManager
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface


def input_decorator_function(func):
    def wrapper(*args, **kwargs):
        transformed_args = tuple(_transform_arg(arg) for arg in args)

        return func(*transformed_args, **kwargs)

    return wrapper


def _transform_arg(arg):
    if isinstance(arg, StringableParameterInterface):
        arg = _transform_arg(arg.to_string())

    if not isinstance(arg, str):
        return arg

    matches = find_all_placeholders(arg)

    if not matches:
        return arg

    parameters = ContainerManager.get_container().get_parameters()

    return replace_all_placeholders(arg, matches, parameters, arg)
