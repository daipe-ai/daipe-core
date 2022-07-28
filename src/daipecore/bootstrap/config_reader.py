from pyfonycore.bootstrap.config.Config import Config


def read() -> Config:
    from pyfonycore.bootstrap.config import config_reader  # pylint: disable=import-outside-toplevel

    return config_reader.read()
