# bot/utils/tg_media.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, ReplyKeyboardMarkup


@dataclass(frozen=True)
class MediaNotFoundError(RuntimeError):
    media_type: str
    file_id: str
    details: str = ""


async def ensure_file_id(
    bot: Bot,
    file_id: str,
    *,
    raise_on_fail: bool = True,
    media_type: str = "file",
) -> bool:
    """
    Validates Telegram file_id by calling get_file().
    Returns True if valid, False otherwise (unless raise_on_fail=True).
    """
    try:
        await bot.get_file(file_id)
        return True
    except TelegramBadRequest as e:
        if raise_on_fail:
            raise MediaNotFoundError(media_type, file_id, str(e)) from e
        return False


async def ensure_video_file_id(bot: Bot, file_id: str, *, raise_on_fail: bool = True) -> bool:
    return await ensure_file_id(bot, file_id, raise_on_fail=raise_on_fail, media_type="video")


async def answer_video_or_raise(
    message: Message,
    *,
    video_id: str,
    caption: Optional[str] = None,
    reply_markup: Optional[ReplyKeyboardMarkup] = None,
    parse_mode: Optional[ParseMode] = None,
) -> None:
    """
    Sends a video by file_id after validating it exists.
    Raises MediaNotFoundError if file_id is invalid/not accessible.
    """
    await ensure_video_file_id(message.bot, video_id, raise_on_fail=True)

    await message.answer_video(
        video=video_id,
        caption=caption,
        reply_markup=reply_markup,
        parse_mode=parse_mode,
    )
