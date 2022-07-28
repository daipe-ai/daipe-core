from daipecore.decorator.InputDecorator import InputDecorator
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator


@DecoratedDecorator
class notebook_function(InputDecorator):  # pylint: disable=invalid-name
    def __init__(self, *args):  # pylint: disable=super-init-not-called
        self._args = args
