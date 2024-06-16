import importlib
from functools import lru_cache

from resources.base_config import BaseConfig


def get_active_env():
    configs_module = importlib.import_module('resources.configs')
    activate_env = getattr(configs_module, "ACTIVATE_ENVIRONMENT")
    classes = [getattr(configs_module, name) for name in dir(configs_module) if name.istitle()]
    for class_item in classes:
        if activate_env == class_item.STAGE:
            return class_item.__name__
    return "Development"


@lru_cache(maxsize=1)
def get_config(config_name: str = None) -> BaseConfig:
    """
    缓存获取激活的配置文件，类单例模式
    """
    if not config_name:
        config_name = get_active_env()

    configs_module = importlib.import_module('resources.configs')
    config_class = getattr(configs_module, config_name.capitalize())
    return config_class()
