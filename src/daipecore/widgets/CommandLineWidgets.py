from daipecore.widgets.Widgets import Widgets
from argparse import ArgumentParser
from daipecore.environment_detector import is_running_in_console


class CommandLineWidgets(Widgets):
    def __init__(self, argument_parser: ArgumentParser):
        self.__argument_parser = argument_parser

    def add_text(self, name: str, default_value: str = None, label: str = None):
        return self.__argument_parser.add_argument("--" + name, dest=name, default=default_value)

    def add_select(self, name: str, choices: list, label: str = None):
        return self.__argument_parser.add_argument("--" + name, dest=name, choices=choices)

    def add_multiselect(self, name: str, choices: list, label: str = None):
        return self.__argument_parser.add_argument("--" + name, nargs="+", dest=name, choices=choices)

    def get_value(self, name: str):
        input_arguments = self.__argument_parser.parse_known_args()[0]
        return input_arguments.__dict__.get(name)

    def should_be_resolved(self):
        return is_running_in_console()
