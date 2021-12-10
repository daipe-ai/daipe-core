import unittest
from box import Box
from daipecore.function import arguments_transformer
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface


class arguments_transformer_test(unittest.TestCase):  # noqa: N801
    def test_basic(self):
        parameters = Box({"base_path": "/foo/bar"})

        result = arguments_transformer.transform("%base_path%/file.txt", parameters)

        self.assertEqual("/foo/bar/file.txt", result)

    def test_stringable_input(self):
        class stringable_class(StringableParameterInterface):  # noqa: N801
            def __init__(self, placeholder_name: str):
                self.__placeholder_name = placeholder_name

            def to_string(self):
                return "%" + self.__placeholder_name + "%"

        parameters = Box({"base_path": "/foo/bar"})

        result = arguments_transformer.transform(stringable_class("base_path"), parameters)

        self.assertEqual("/foo/bar", result)


if __name__ == "__main__":
    unittest.main()
