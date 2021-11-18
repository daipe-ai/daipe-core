from pyfonycore.bootstrap.config.Config import Config


def read() -> Config:
    from pyfonycore.bootstrap.config import config_reader

    return config_reader.read()
