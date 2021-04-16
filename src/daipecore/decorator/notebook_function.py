from daipecore.decorator.InputDecorator import InputDecorator
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator


@DecoratedDecorator
class notebook_function(InputDecorator):  # noqa: N801
    def __init__(self, *args):
        self._args = args
