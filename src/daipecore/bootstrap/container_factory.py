from injecta.container.ContainerInterface import ContainerInterface


def create_container(app_env: str) -> ContainerInterface:
    from daipecore.bootstrap.config import bootstrap_config

    return bootstrap_config.container_init_function(app_env, bootstrap_config)
