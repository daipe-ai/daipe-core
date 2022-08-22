from typing import List
from daipecore.widgets.Widgets import Widgets
from daipecore.widgets.CommandLineWidgets import CommandLineWidgets


class WidgetsFactory:
    def __init__(self, widgets: List[Widgets], cli_widgets: CommandLineWidgets):
        self.__widgets = widgets
        self.__cli_widgets = cli_widgets

    def create(self) -> Widgets:
        for widget in self.__widgets:
            if widget.should_be_resolved():
                return widget

        return self.__cli_widgets
