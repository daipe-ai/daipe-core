import sys
import unittest
from argparse import ArgumentError
from daipecore.widgets.CommandLineWidgets import CommandLineWidgets
from daipecore.widgets.TestingArgumentParser import TestingArgumentParser


class CommandLineWidgetsTest(unittest.TestCase):
    def setUp(self):
        self.__command_line_widgets = CommandLineWidgets(TestingArgumentParser())

    def test_widget_text_as_list(self):
        self.__command_line_widgets.add_text("mytext")
        sys.argv = ["test", "--mytext", "January, February"]
        self.assertEqual("January, February", self.__command_line_widgets.get_value("mytext"))

    def test_widget_select(self):
        self.__command_line_widgets.add_select("myselect", ["month", "year"])
        sys.argv = ["test", "--myselect", "year"]
        self.assertEqual("year", self.__command_line_widgets.get_value("myselect"))

    def test_widget_select_invalid_value(self):
        with self.assertRaises(ArgumentError) as error:
            self.__command_line_widgets.add_select("myselect", ["month", "year"])

            sys.argv = ["test", "--myselect", "xxx"]
            self.__command_line_widgets.get_value("myselect")

        self.assertEqual("argument --myselect: invalid choice: 'xxx' (choose from 'month', 'year')", str(error.exception))

    def test_widget_multiselect_all_values(self):
        self.__command_line_widgets.add_multiselect("mymulti", ["January", "February", "March"])
        sys.argv = ["test", "--mymulti", "January", "February"]
        self.assertEqual(["January", "February"], self.__command_line_widgets.get_value("mymulti"))

    def test_widget_multiselect_one_value(self):
        self.__command_line_widgets.add_multiselect("mymulti", ["January", "February", "March"])
        sys.argv = ["test", "--mymulti", "January"]
        self.assertEqual(["January"], self.__command_line_widgets.get_value("mymulti"))

    def test_exception_multiselect_not_part_of_selection_one_value(self):
        with self.assertRaises(Exception) as error:
            self.__command_line_widgets.add_multiselect("mymulti", ["January", "February", "March"])

            sys.argv = ["test", "--mymulti", "April"]
            self.__command_line_widgets.get_value("mymulti")

        self.assertEqual("argument --mymulti: invalid choice: 'April' (choose from 'January', 'February', 'March')", str(error.exception))

    def test_exception_multiselect_not_part_of_selection_more_values(self):
        with self.assertRaises(Exception) as error:
            self.__command_line_widgets.add_multiselect("mymulti", ["January", "February", "March"])

            sys.argv = ["test", "--mymulti", "January", "April"]
            self.__command_line_widgets.get_value("mymulti")

        self.assertEqual(
            "argument --mymulti: invalid choice: 'April' (choose from 'January', 'February', 'March')",
            str(error.exception),
        )


if __name__ == "__main__":
    unittest.main()
