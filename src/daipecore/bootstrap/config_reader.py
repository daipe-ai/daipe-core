import os
from pathlib import Path
from pyfonycore.bootstrap.config.Config import Config
from daipecore.environment_detector import is_jupyter_server_running


def set_jupyter_cwd():
    from jupyter_server import serverapp

    running_servers = list(serverapp.list_running_servers())
    for item in running_servers:
        if Path(item["root_dir"]).resolve() in Path.cwd().parents:
            return os.chdir(item["root_dir"])


def read() -> Config:
    if is_jupyter_server_running():
        set_jupyter_cwd()

    from pyfonycore.bootstrap.config import config_reader

    return config_reader.read()
