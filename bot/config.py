from os import environ as env

class Telegram:
    API_ID = 23028247
    API_HASH = "659c5f1124a81ad789a6ea021da73f4d"
    BOT_TOKEN = "6810418594:AAFKZkzxQ9YkP3By6jdzu8m-Dhimiu0im0c"
    OWNER_ID = 6383913878
    ALLOWED_USER_IDS = ""
    BOT_USERNAME = "pdupload_bot"
    CHANNEL_ID = -1002105902998
    SECRET_CODE_LENGTH = 4

class Server:
    BASE_URL = "https://dls.thekvt.eu.org"
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
