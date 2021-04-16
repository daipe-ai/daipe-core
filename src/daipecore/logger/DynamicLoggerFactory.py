from logging import Logger


class DynamicLoggerFactory:
    def __init__(
        self,
        logger_factory,
    ):
        self.__logger_factory = logger_factory

    def create(self) -> Logger:
        return self.__logger_factory.create()
