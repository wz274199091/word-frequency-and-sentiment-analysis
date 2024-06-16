class BaseConfig:
    """
    通用的配置类
    """
    # 端口
    PORT = 39801

    # 日志配置
    LOGGING_LEVEL: str = 'DEBUG'

    LOG_FILE_PATH: str = './logs'

    LOGGING_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(asctime)s %(levelprefix)s %(message)s",  # 这里日志格式加了时间显示
                "use_colors": False,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(name)s %(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
                # 这里日志格式加了时间显示
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "default_file": {
                "formatter": "default",
                "class": "nb_log.handlers.BothDayAndSizeRotatingFileHandler",  # 注意这里是多进程安全切割日志
                'file_name': 'uvicorn_default.log',
                'log_path': LOG_FILE_PATH,
                'max_bytes': 1000 * 1000 * 1000,
                'back_count': 10,

            },

            "access": {
                "formatter": "access",
                "class": "nb_log.handlers.ColorHandler",  # 这里用了nb_log的彩色控制台handler。
            },
            "access_file": {
                "formatter": "access",
                "class": "nb_log.handlers.BothDayAndSizeRotatingFileHandler",  # 注意这里是多进程安全切割日志
                'file_name': 'uvicorn_access.log',
                'log_path': LOG_FILE_PATH,
                'max_bytes': 1000 * 1000 * 1000,
                'back_count': 10,
            },
        },
        "loggers": {
            "uvicorn": {"handlers": ["default", "default_file"], "level": "INFO"},
            "uvicorn.error": {"level": "INFO"},
            "uvicorn.access": {"handlers": ["access", "access_file"], "level": "INFO", "propagate": False},
        },
    }
