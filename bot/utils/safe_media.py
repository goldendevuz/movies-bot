# bot/utils/safe_media.py
from __future__ import annotations

from typing import Optional

from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, ReplyKeyboardMarkup

from bot.utils.tg_media import ensure_video_file_id


async def safe_answer_video(
    message: Message,
    *,
    video_id: str,
    caption: Optional[str] = None,
    reply_markup: Optional[ReplyKeyboardMarkup] = None,
    parse_mode: Optional[ParseMode] = None,
    not_found_text: Optional[str] = "❌ Video topilmadi yoki file_id xato.",
) -> bool:
    """
    Safely sends a video by file_id.
    - Returns True if sent
    - Returns False if file_id is invalid or not found
    - NEVER raises TelegramBadRequest
    """
    try:
        ok = await ensure_video_file_id(message.bot, video_id, raise_on_fail=False)
        if not ok:
            if not_found_text:
                await message.answer(not_found_text)
            return False

        await message.answer_video(
            video=video_id,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode=parse_mode,
        )
        return True

    except TelegramBadRequest:
        # In case send itself fails (e.g., file became unavailable between get_file and send)
        if not_found_text:
            await message.answer(not_found_text)
        return False
