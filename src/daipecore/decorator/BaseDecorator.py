from typing import Callable, Tuple, Optional


class BaseDecorator:
    _is_decorator = (
        True
        # use this instead of isinstance(decorator_argument, InputDecorator) which does not work probably due to some cyclic import
    )

    _args: Tuple = tuple()
    _function: Callable = lambda: None
    _previous_decorator_instance: Optional["BaseDecorator"] = None

    @property
    def function(self):
        return self._function

    def set_function(self, function: Callable):
        self._function = function  # pyre-ignore[8]

    @property
    def previous_decorator_instance(self):
        return self._previous_decorator_instance

    def set_previous_decorator_instance(self, previous_decorator_instance: Optional["BaseDecorator"] = None):
        self._previous_decorator_instance = previous_decorator_instance

    def __call__(self, *args, **kwargs):
        pass
