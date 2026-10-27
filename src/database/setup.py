from tortoise import Tortoise

from src.config import TORTOISE_ORM


async def init_db() -> None:
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)
    print("Bot started.")


async def close_db() -> None:
    await Tortoise.close_connections()
    print("Bot stopped.")
