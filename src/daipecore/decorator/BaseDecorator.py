class BaseDecorator:
    _is_decorator = (
        True
        # use this instead of isinstance(decorator_argument, InputDecorator) which does not work probably due to some cyclic import
    )

    _args: tuple = tuple()
    _function: callable = lambda: None
    _previous_decorator_instance: "BaseDecorator" = None

    @property
    def function(self):
        return self._function

    def set_function(self, function: callable):
        self._function = function

    @property
    def previous_decorator_instance(self):
        return self._previous_decorator_instance

    def set_previous_decorator_instance(self, previous_decorator_instance: "BaseDecorator" = None):
        self._previous_decorator_instance = previous_decorator_instance

    def __call__(self, *args, **kwargs):
        pass
