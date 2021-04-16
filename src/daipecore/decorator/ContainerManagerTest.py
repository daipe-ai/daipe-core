import os
import unittest
from injecta.container.ContainerInterface import ContainerInterface
from daipecore.decorator.ContainerManager import ContainerManager


class ContainerManagerTest(unittest.TestCase):
    def test_basic(self):
        os.environ["APP_ENV"] = "test"

        container = ContainerManager.get_container()

        self.assertIsInstance(container, ContainerInterface)


if __name__ == "__main__":
    unittest.main()
