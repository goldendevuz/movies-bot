from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons.reply import build_reply_button
from bot.dispatcher import dp
from bot.handler.main_menu import SectorState
from bot.utils.safe_media import safe_answer_video


@dp.message(SectorState.movies_section, F.text == __("🎭 Drama"))
@dp.message(SectorState.yes_hand_drama_titanic, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_drama_joker, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_drama_whale, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_drama_forrest_gump, F.text == __("⬅️ Back"))
@dp.message(SectorState.whale, F.text == __("⬅️ Back"))
@dp.message(SectorState.forest_gump, F.text == __("⬅️ Back"))
@dp.message(SectorState.titanic, F.text == __("⬅️ Back"))
async def dramas_handler(message: Message, state: FSMContext):
    texts = [_("🎬 Forrest Gump (1994)"), _("🎬 Titanic (1997)"), _("🎬 Joker (2019)"), _("🎬 The Whale (2022)"),
             _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 2, 1))
    await state.set_state(SectorState.dramas_section)
    await message.answer(_("Choose the movie."), reply_markup=markup)


@dp.message(SectorState.dramas_section, F.text == __("🎬 Forrest Gump (1994)"))
async def forrest_gump(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Forrest Gump (1994)</b>\n"
        "⭐ <b>IMDb Rating</b>: 8.8/10\n"
        "🎭 <b>Genre</b>: Drama, Romance\n"
        "🎥 <b>Director</b>: Robert Zemeckis\n"
        "👤 <b>Starring</b>: Tom Hanks, Robin Wright, Gary Sinise\n"
        "🏆 <b>Awards</b>: Won 6 Academy Awards, including Best Picture 🎬 & Best Actor (Tom Hanks) 🏅\n"
        "📖 <b>Plot Summary</b>: Forrest Gump is a kind-hearted man with a low IQ but an extraordinary life. "
        "He unwittingly takes part in major historical events, fighting in the Vietnam War, becoming a table tennis champion, "
        "and even investing in Apple. However, his true dream is to reunite with his childhood love, Jenny.\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.forest_gump)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.forest_gump, F.text == __("Yes"))
async def yes_handler(message: Message, state: FSMContext):
    video_id = "BAACAgIAAxkBAAINLWhwpE_rZ_cvr6VifZoO-aqNWXqqAALkYgAC9XK5SeqQVnNkPDoRNgQ"

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    markup = rkb.as_markup(resize_keyboard=True)

    await state.set_state(SectorState.yes_hand_drama_forrest_gump)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Forrest Gump (1994)"),
        reply_markup=markup,
    )


@dp.message(SectorState.dramas_section, F.text == __("🎬 Titanic (1997)"))
async def titanic(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Titanic (1997)</b>\n"
        "⭐ <b>IMDb Rating</b>: 7.9/10\n"
        "🎭 <b>Genre</b>: Drama, Romance\n"
        "🎥 <b>Director</b>: James Cameron\n"
        "👤 <b>Starring</b>: Leonardo DiCaprio, Kate Winslet, Billy Zane\n"
        "🏆 <b>Awards</b>: Won 11 Academy Awards 🏅\n"
        "📖 <b>Plot Summary</b>: A young artist named Jack and an upper-class woman named Rose meet and fall in love "
        "aboard the ill-fated RMS Titanic. Despite their different social backgrounds, their romance blossoms as "
        "the ship sails towards its tragic destiny. As disaster strikes, their love is put to the ultimate test "
        "in this unforgettable cinematic masterpiece. 🚢💔\n\n"
        "Do you want to watch it?"

    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.titanic)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.titanic, F.text == __("Yes"))
async def yes_handler_drama_titanic(message: Message, state: FSMContext):
    video_id = "BAACAgQAAxkBAAINWGhwrTcXiyFdYz9nX1OAIke9WnhJAAKRBwACnXcZUW6NfGgXi-Q_NgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_drama_titanic)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Titanic (1997)"),
        reply_markup=rkb,
    )


@dp.message(SectorState.dramas_section, F.text == __("🎬 Joker (2019)"))
async def joker(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Joker (2019)</b>\n"
        "⭐ <b>IMDb Rating</b>: 8.4/10\n"
        "🎭 <b>Genre</b>: Crime, Drama, Thriller\n"
        "🎥 <b>Director</b>: Todd Phillips\n"
        "👤 <b>Starring</b>: Joaquin Phoenix, Robert De Niro, Zazie Beetz\n"
        "🏆 <b>Awards</b>: Won 2 Academy Awards 🏅\n"
        "📖 <b>Plot Summary</b>: Arthur Fleck, a struggling comedian with a troubled past, descends into madness as "
        "he faces constant rejection and societal neglect. In a city filled with crime and despair, his transformation "
        "into the infamous Joker becomes inevitable. A haunting psychological thriller that explores the origins "
        "of Gotham's most notorious villain. 🤡🔥\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.joker)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.joker, F.text == __("Yes"))
async def yes_handler_drama_titanic(message: Message, state: FSMContext):
    video_id = "BAACAgQAAxkBAAINWGhwrTcXiyFdYz9nX1OAIke9WnhJAAKRBwACnXcZUW6NfGgXi-Q_NgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_drama_joker)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Joker (2019)"),
        reply_markup=rkb,
    )
    

@dp.message(SectorState.dramas_section, F.text == __("🎬 The Whale (2022)"))
async def whale(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>The Whale (2022)</b>\n"
        "⭐ <b>IMDb Rating</b>: 7.7/10\n"
        "🎭 <b>Genre</b>: Drama\n"
        "🎥 <b>Director</b>: Darren Aronofsky\n"
        "👤 <b>Starring</b>: Brendan Fraser, Sadie Sink, Hong Chau\n"
        "🏆 <b>Awards</b>: Won 2 Academy Awards 🏅\n"
        "📖 <b>Plot Summary</b>: Charlie, a reclusive and severely obese English teacher, struggles to reconnect "
        "with his estranged teenage daughter. As he battles his own guilt and health issues, he seeks redemption "
        "and a final chance to make things right. A deeply emotional and powerful story of love, regret, and "
        "forgiveness.\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.whale)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.whale, F.text == __("Yes"))
async def yes_handler_drama_titanic(message: Message, state: FSMContext):
    video_id = "BAACAgIAAxkBAAINYGhwramd5nceoLKPM23pi56FUY1oAAKDZAAC9XLBSYqpzAQxKl-ENgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_drama_whale)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 The Whale (2022)"),
        reply_markup=rkb,
    )
