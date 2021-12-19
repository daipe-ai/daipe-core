import unittest
from box import Box
from daipecore.function import arguments_transformer
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface
from injecta.container.ContainerInterface import ContainerInterface


class FakeContainer(ContainerInterface):
    def __init__(self, parameters: Box):
        self.__parameters = parameters

    def get_parameters(self) -> Box:
        return self.__parameters

    def get(self, ident):
        raise Exception("Method must not be called")


class arguments_transformer_test(unittest.TestCase):  # noqa: N801
    def test_basic(self):
        container = FakeContainer(Box({"base_path": "/foo/bar"}))

        result = arguments_transformer.transform("%base_path%/file.txt", container)

        self.assertEqual("/foo/bar/file.txt", result)

    def test_stringable_input(self):
        class stringable_class(StringableParameterInterface):  # noqa: N801
            def __init__(self, placeholder_name: str):
                self.__placeholder_name = placeholder_name

            def to_string(self):
                return "%" + self.__placeholder_name + "%"

        container = FakeContainer(Box({"base_path": "/foo/bar"}))

        result = arguments_transformer.transform(stringable_class("base_path"), container)

        self.assertEqual("/foo/bar", result)


if __name__ == "__main__":
    unittest.main()
