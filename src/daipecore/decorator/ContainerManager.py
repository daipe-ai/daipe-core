import os
from injecta.container.ContainerInterface import ContainerInterface


class ContainerManager:

    _container: ContainerInterface

    @classmethod
    def set_container(cls, container: ContainerInterface):
        cls._container = container

    @classmethod
    def get_container(cls):
        if not hasattr(cls, "_container"):
            cls._container = cls._create_container()

        return cls._container

    @staticmethod
    def _create_container():
        from daipecore.bootstrap.config import bootstrap_config
        from daipecore.bootstrap.container_factory import create_container

        if "APP_ENV" not in os.environ:
            raise Exception(f"Set APP_ENV env variable to define environment ({', '.join(bootstrap_config.allowed_environments)})")

        return create_container(os.environ["APP_ENV"])
