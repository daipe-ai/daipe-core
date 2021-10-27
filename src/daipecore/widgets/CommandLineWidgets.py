from daipecore.widgets.Widgets import Widgets
from argparse import ArgumentParser
from daipecore.detector import is_cli


class CommandLineWidgets(Widgets):
    def __init__(self, argument_parser: ArgumentParser):
        self.__argument_parser = argument_parser

    def add_text(self, name: str, default_value: str = "", label: str = None):
        self.__argument_parser.add_argument("--" + name, dest=name, default=default_value, help=label)

    def add_select(self, name: str, choices: list, default_value: str, label: str = None):
        if None in choices:
            raise Exception("Value None cannot be used as choice, use empty string instead")

        if default_value not in choices:
            raise Exception(f'Default value "{default_value}" not among choices')

        self.__argument_parser.add_argument("--" + name, dest=name, choices=choices, default=default_value, help=label, required=False)

    def add_multiselect(self, name: str, choices: list, default_values: list, label: str = None):
        self.__argument_parser.add_argument(
            "--" + name, nargs="+", dest=name, choices=choices, default=default_values, help=label, required=False
        )

    def remove(self, name: str):
        pass

    def remove_all(self):
        pass

    def get_value(self, name: str):
        input_arguments = self.__argument_parser.parse_known_args()[0]
        values = input_arguments.__dict__

        if name not in values:
            raise Exception(f'No widget defined for name "{name}"')

        value = values.get(name)

        if value is None:
            return ""

        return value

    def should_be_resolved(self):
        return is_cli()
