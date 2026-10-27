import os

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("bot_token")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable is not set.")
BOT_USERNAME = os.getenv("bot_username")
BOT_ID = os.getenv("bot_id")
BOT_PROXY = os.getenv("bot_proxy")
DB_URL = os.getenv("db_url")
if DB_URL is None:
    raise ValueError("DB_URL environment variable is not set.")

TORTOISE_ORM = {
    "connections": {
        "default": DB_URL,
    },
    "apps": {
        "models": {
            "models": ["src.database.models"],
            "default_connection": "default",
            "migrations": "src.database.migrations",
        },
    },
}
