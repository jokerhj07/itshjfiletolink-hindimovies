from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 26917100))
    API_HASH = env.get("TELEGRAM_API_HASH", "b440ca1a19af5fc71ceaae0dabbfb779")
    OWNER_ID = int(env.get("OWNER_ID", 6026244374))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "6026244374").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "itshjfiletolinkbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7929561832:AAGaB8GTF2f9AfI0yIdK9PpN23F4F_mrJJ8")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1004207509675))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://itshjfiletolink-hindimovies.onrender.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
