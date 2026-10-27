import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import BotCommand

from src.config import BOT_PROXY, BOT_TOKEN
from src.database.setup import close_db, init_db
from src.middlewares import RegistrarMiddleware
from src.routers import rs

logger = logging.getLogger(__name__)

dp = Dispatcher()
dp.include_routers(*rs)
dp.update.outer_middleware.register(RegistrarMiddleware())


async def set_commands(bot: Bot) -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start the bot"),
        ]
    )


dp.startup.register(init_db)
dp.startup.register(set_commands)
dp.shutdown.register(close_db)

if BOT_PROXY:
    try:
        bot = Bot(BOT_TOKEN, session=AiohttpSession(proxy=BOT_PROXY))
    except RuntimeError as exc:
        if "aiohttp-socks" in str(exc).lower():
            logger.warning(
                "Proxy configured but dependency aiohttp-socks is missing. "
                "Falling back to direct connection."
            )
            bot = Bot(BOT_TOKEN)
        else:
            raise
else:
    bot = Bot(BOT_TOKEN)

__all__ = ["bot", "dp"]
