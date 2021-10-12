import _ast
from daipecore.lineage.argument.FunctionCallAttribute import FunctionCallAttribute
from daipecore.lineage.argument.FunctionLink import FunctionLink
from daipecore.lineage.argument.ArgumentClassResolver import ArgumentClassResolver
from daipecore.decorator.utils import get_decorator_id


class ArgumentParser:
    def __init__(self, function_argument_parser_resolver: ArgumentClassResolver):
        self.__function_argument_parser_resolver = function_argument_parser_resolver

    def parse(self, arg: _ast.expr):
        if isinstance(arg, _ast.Call):  # called function like read_table("my_table")
            argument_class = self.__function_argument_parser_resolver.resolve(get_decorator_id(arg))
            return argument_class(*[self.parse(subarg) for subarg in arg.args])

        if isinstance(arg, _ast.Name):  # function name like my_previous_notebook_function
            return FunctionLink(arg.id)

        if isinstance(arg, _ast.Attribute):  # attribute of possible function call: table_params("my_table").some_attribute
            return FunctionCallAttribute(self.parse(arg.value), arg.attr)

        if isinstance(arg, _ast.Constant):
            return arg.value

        if hasattr(_ast, "Str") and isinstance(arg, _ast.Str):
            return arg.s

        raise Exception(f"Unexpected argument type: {type(arg)}")
