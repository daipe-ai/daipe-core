import sys
import builtins


def is_jupyter_server_running():
    return "ipykernel" in sys.modules


def is_running_in_console():
    return not hasattr(builtins, "__IPYTHON__")
