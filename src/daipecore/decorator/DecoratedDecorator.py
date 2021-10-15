# inspired by https://stackoverflow.com/a/1594484
import inspect
import types
import re
from daipecore.decorator.ContainerManager import ContainerManager
from daipecore.decorator.InputDecorator import InputDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator


class DecoratedDecorator:
    def __init__(self, original_decorator):
        self._original_decorator = original_decorator

    def __call__(self, *args, **kwargs):
        if args and isinstance(args[0], types.FunctionType):
            code = inspect.getsource(args[0])

            match = re.match(r"^\s*@[a-z_]+([\(]?)", code)

            if match and match.group(1) == "":
                decorator_name = self._original_decorator.__name__
                raise Exception(f"Use @{decorator_name}() instead of @{decorator_name} please")

        decorator_args = args
        decorator_kwargs = kwargs

        def wrapper(func):
            decorator_instance = self._original_decorator(*decorator_args, **decorator_kwargs, func=func)
            decorated_function: callable = decorator_instance.function

            if decorated_function.__module__ != "__main__":
                return func

            if isinstance(decorator_instance, InputDecorator) and decorator_instance.immediate_execution_enabled:
                container = ContainerManager.get_container()

                processed_arguments = decorator_instance.prepare_arguments(container)
                result = decorated_function(*processed_arguments)

                decorator_instance.set_result(result)

                decorator_instance.after_execution(container)

                previous_decorator_instance = decorator_instance.previous_decorator_instance

                if isinstance(previous_decorator_instance, OutputDecorator):
                    previous_decorator_instance.process_result(result, container)

            return decorator_instance

        return wrapper

    def __instancecheck__(self, instance):
        return isinstance(instance, self._original_decorator)
