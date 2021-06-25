from typing import List
from daipecore.widgets.Widgets import Widgets


class WidgetsFactory:
    def __init__(self, widgets: List[Widgets]):
        self.__widgets = widgets

    def create(self) -> Widgets:
        for widget in self.__widgets:
            if widget.should_be_resolved():
                return widget
        raise Exception("No widgets resolved")
