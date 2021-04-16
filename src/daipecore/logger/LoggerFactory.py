import pathlib
from logging import Logger
from loggerbundle.LoggerFactory import LoggerFactory as OriginalLoggerFactory


class LoggerFactory:
    def __init__(
        self,
        logger_factory: OriginalLoggerFactory,
    ):
        self.__logger_factory = logger_factory

    def create(self) -> Logger:
        notebook_path = pathlib.Path().absolute()

        return self.__logger_factory.create(str(notebook_path))
