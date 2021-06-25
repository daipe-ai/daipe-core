from injecta.container.ContainerInterface import ContainerInterface
from daipecore.function.input_decorator_function import input_decorator_function
from daipecore.widgets.Widgets import Widgets


@input_decorator_function
def get_widget_value(name: str):
    def wrapper(container: ContainerInterface):
        widgets: Widgets = container.get("daipecore.widgets.Widgets")
        return widgets.get_value(name)

    return wrapper
