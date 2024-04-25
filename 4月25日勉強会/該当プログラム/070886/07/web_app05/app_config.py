def dict_config():
    return {
    'version': 1,
    'formatters': {
        'file': {
            'format': '[%(asctime)s] [%(levelname)s] : %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'filename': './logs/app.log',
            'encoding': 'utf-8'     #日本語化けないように
        }
    },
    'root': {
        'level': 'WARN',
        'handlers': ['file']        #フォルダーは作っておく
    },
}