from box import Box
from injecta.parameter.all_placeholders_replacer import find_all_placeholders, replace_all_placeholders
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface


def transform(arg, parameters: Box):
    if isinstance(arg, StringableParameterInterface):
        arg = transform(arg.to_string(), parameters)

    if not isinstance(arg, str):
        return arg

    matches = find_all_placeholders(arg)

    if not matches:
        return arg

    return replace_all_placeholders(arg, matches, parameters, arg)
