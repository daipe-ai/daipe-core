import builtins


def is_cli():
    return not hasattr(builtins, "__IPYTHON__")  # False if running in ipython console
