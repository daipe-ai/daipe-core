import types
from injecta.container.ContainerInterface import ContainerInterface
from injecta.parameter.all_placeholders_replacer import find_all_placeholders, replace_all_placeholders
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface


def transform(arg, container: ContainerInterface):
    if isinstance(arg, StringableParameterInterface):
        arg = transform(arg.to_string(), container)

    if isinstance(arg, types.FunctionType):
        arg = transform(arg()(container), container)

    if not isinstance(arg, str):
        return arg

    matches = find_all_placeholders(arg)

    if not matches:
        return arg

    return replace_all_placeholders(arg, matches, container.get_parameters(), arg)
