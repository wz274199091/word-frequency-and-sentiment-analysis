import multiprocessing

from resources.base_config import BaseConfig

ACTIVATE_ENVIRONMENT = "test"


class Development(BaseConfig):
    STAGE: str = 'dev'

    PORT = 33339

    WORKERS = 1

    RELOAD = False


class Test(BaseConfig):
    STAGE: str = 'test'

    PORT = 33330

    WORKERS = 1

    RELOAD = False


class Production(BaseConfig):
    STAGE: str = 'prd'

    PORT = 33335

    WORKERS = 1

    RELOAD = False
