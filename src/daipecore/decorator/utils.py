import ast


def is_decorator(decorator: ast.Call) -> bool:
    return hasattr(decorator.func, "id") or hasattr(decorator.func, "attr")


def get_decorator_id(decorator: ast.Call) -> str:
    if isinstance(decorator.func, ast.Name):
        return decorator.func.id
    elif isinstance(decorator.func, ast.Attribute):
        return decorator.func.attr
    else:
        raise Exception(f"{decorator.func} is neither ast.Name nor ast.Attribute")
