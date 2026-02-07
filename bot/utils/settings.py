import os

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from db.base import db as database


def _parse_admin_ids() -> list[int]:
    raw = (os.getenv("ADMINS_IDS") or "").strip()
    if not raw:
        return []
    ids: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            ids.append(int(part))
        except ValueError:
            # noto'g'ri qiymatlarni jim o'tkazib yuboramiz
            continue
    return ids


ADMINS_IDS = _parse_admin_ids()


async def on_startup(bot: Bot):
    await database.create_all()

    # Global (hamma uchun) komandalar
    commands = [
        BotCommand(command="start", description="boshlash"),
        BotCommand(command="help", description="yordam"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    # Admin komandasi (faqat admin chat scope)
    if ADMINS_IDS:
        admin_commands = [BotCommand(command="admin", description="admin panel")]
        for admin_id in ADMINS_IDS:
            try:
                await bot.set_my_commands(
                    admin_commands,
                    scope=BotCommandScopeChat(chat_id=admin_id),
                )
            except Exception:
                # Admin chat topilmasa (botga hali yozmagan bo'lsa) yiqitmaymiz
                pass


async def on_shutdown():
    pass
