from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons.reply import build_reply_button
from bot.dispatcher import dp
from bot.states import SectorState
from bot.utils.safe_media import safe_answer_video


@dp.message(SectorState.movies_section, F.text == __("🎬 Action"))
@dp.message(SectorState.damsel, F.text == __("⬅️ Back"))
@dp.message(SectorState.avengers, F.text == __("⬅️ Back"))
@dp.message(SectorState.fury, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_action_avengers, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_action_fury, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_action_smiths, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_action_damsel, F.text == __("⬅️ Back"))
@dp.message(SectorState.mr_mrs_smith, F.text == __("⬅️ Back"))
async def action_handler(message: Message, state: FSMContext):
    texts = [_("🎬 Mr. & Mrs.Smith (2005)"), _("🎬 Damsel (2024)"), _("🎬 Avengers: Endgame (2019)"), _("🎬 Fury (2014)"),
             _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 2, 1))
    await state.set_state(SectorState.action_section)
    await message.answer(_("Choose the movie."), reply_markup=markup)


@dp.message(SectorState.action_section, F.text == __("🎬 Mr. & Mrs.Smith (2005)"))
async def smiths(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Mr. & Mrs. Smith (2005)</b>\n"
        "⭐ <b>IMDb Rating</b>: 6.5/10\n"
        "🎭 <b>Genre</b>: Action, Comedy, Romance\n"
        "🎥 <b>Director</b>: Doug Liman\n"
        "👤 <b>Starring</b>: Brad Pitt, Angelina Jolie, Vince Vaughn\n"
        "🏆 <b>Awards</b>: Nominated for 1 MTV Movie Award 🏅\n"
        "📖 <b>Plot Summary</b>: John and Jane Smith appear to be a normal married couple, but both of them are secretly highly skilled assassins working for rival organizations. When they are assigned to eliminate each other, their mundane marriage turns into an explosive battle filled with action, humor, and romance. Can love survive when the mission is to kill?\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.mr_mrs_smith)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.mr_mrs_smith, F.text == __("Yes"))
async def yes_handler_action_smiths(message: Message, state: FSMContext):
    video_id = "BAACAgQAAxkBAAINlWhwr_TOs3jOqmiyZGM6qhHPm5KBAAIBFwACbmzgUQVjA0HPIsFuNgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_action_smiths)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Mr. & Mrs.Smith (2005)"),
        reply_markup=rkb,
    )


@dp.message(SectorState.action_section, F.text == __("🎬 Damsel (2024)"))
async def damsel(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Damsel (2024)</b>\n"
        "⭐ <b>IMDb Rating</b>: N/A (Upcoming Release)\n"
        "🎭 <b>Genre</b>: Fantasy, Action, Adventure\n"
        "🎥 <b>Director</b>: Juan Carlos Fresnadillo\n"
        "👤 <b>Starring</b>: Millie Bobby Brown, Angela Bassett, Robin Wright\n"
        "🏆 <b>Awards</b>: N/A 🏅\n"
        "📖 <b>Plot Summary</b>: Elodie, a young princess, agrees to marry a prince from a wealthy kingdom, believing "
        "she is securing peace. However, she soon realizes she has been chosen as a sacrifice to an ancient dragon. "
        "Trapped in a deadly labyrinth, Elodie must rely on her intelligence, courage, and determination to escape. "
        "A thrilling tale of survival and empowerment!\n\n"
        "Do you want to watch it?"

    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.damsel)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.damsel, F.text == __("Yes"))
async def yes_handler_action_damsel(message: Message, state: FSMContext):
    video_id = "BAACAgQAAxkBAAINnGhwsKvVJP1SATfldj_ZwQGLEtdpAAIjEAAC-gpxUNTOaApt2R4kNgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_action_damsel)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Damsel (2024)"),
        reply_markup=rkb,
    )


@dp.message(SectorState.action_section, F.text == __("🎬 Avengers: Endgame (2019)"))
async def avengers(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Avengers: Endgame (2019)</b>\n"
        "⭐ <b>IMDb Rating</b>: 8.4/10\n"
        "🎭 <b>Genre</b>: Action, Adventure, Drama\n"
        "🎥 <b>Director</b>: Anthony Russo, Joe Russo\n"
        "👤 <b>Starring</b>: Robert Downey Jr., Chris Evans, Mark Ruffalo, Scarlett Johansson\n"
        "🏆 <b>Awards</b>: Won 1 Academy Award, Nominated for 1 more 🏅\n"
        "📖 <b>Plot Summary</b>: After the devastating events of Infinity War, the surviving Avengers must band "
        "together to restore balance to the universe. Facing their biggest challenge yet, they embark on a time-bending"
        " mission to bring back their fallen allies and defeat Thanos once and for all. An epic conclusion to the "
        "Marvel Cinematic Universe's Infinity Saga! ⚡\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.avengers)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.avengers, F.text == __("Yes"))
async def yes_handler_action_avengers(message: Message, state: FSMContext):
    video_id = "BAACAgIAAxkBAAINoGhwsMfCaEyFTPPkNHhCfnt0uLXkAAK3AwAC9k5BSny9_2LjpqRcNgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.yes_hand_action_avengers)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Avengers: Endgame (2019)"),
        reply_markup=rkb,
    )


@dp.message(SectorState.action_section, F.text == __("🎬 Fury (2014)"))
async def fury(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Fury (2014)</b>\n"
        "⭐ <b>IMDb Rating</b>: 7.6/10\n"
        "🎭 <b>Genre</b>: Action, Drama, War\n"
        "🎥 <b>Director</b>: David Ayer\n"
        "👤 <b>Starring</b>: Brad Pitt, Shia LaBeouf, Logan Lerman\n"
        "🏆 <b>Awards</b>: Nominated for 1 Academy Award 🏅\n"
        "📖 <b>Plot Summary</b>: In the final months of World War II, a battle-hardened U.S. Army sergeant named "
        "Wardaddy leads a five-man crew in a Sherman tank called 'Fury' on a deadly mission behind enemy lines. "
        "Vastly outnumbered and facing relentless German forces, they must fight together to survive in one of the "
        "most intense war films ever made. A gripping tale of courage and sacrifice!\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.fury)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.fury, F.text == __("Yes"))
async def yes_handler_action_fury(message: Message, state: FSMContext):
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True)
    video_id = "BAACAgIAAxkBAAINoGhwsMfCaEyFTPPkNHhCfnt0uLXkAAK3AwAC9k5BSny9_2LjpqRcNgQ"
    await state.set_state(SectorState.yes_hand_action_fury)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Fury (2014)"),
        reply_markup=rkb,
    )
