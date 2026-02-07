from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons.reply import build_reply_button
from bot.dispatcher import dp
from bot.states import SectorState
from bot.utils.safe_media import safe_answer_video


@dp.message(SectorState.movies_section, F.text == __("😂 Comedy"))
@dp.message(SectorState.yes_hand_comedy, F.text == __("⬅️ Back"))
@dp.message(SectorState.yes_hand_comedy_dump, F.text == __("⬅️ Back"))
@dp.message(SectorState.home_alone, F.text == __("⬅️ Back"))
async def comedy_handler(message: Message, state: FSMContext):
    texts = [_("🎬 Home Alone (1990)"), _("⬅️ Back")]
    # _("🎬 Dumb and Dumber (1994)"), _("🎬 The Mask (1994)"),
    # _("🎬 Mrs. Doubtfire (1993)"),
    markup = build_reply_button(texts, (2, 2, 1))
    await state.set_state(SectorState.comedy_section)
    await message.answer(_("Choose the movie."), reply_markup=markup)


@dp.message(F.text == __("🎬 Home Alone (1990)"))
async def home_alone(message: Message, state: FSMContext):
    text = (_(
        "🎬 <b>Home Alone (1990)</b>\n"
        "⭐ <b>IMDb Rating</b>: 7.7/10\n"
        "🎭 <b>Genre</b>: Comedy, Family\n"
        "🎥 <b>Director</b>: Chris Columbus\n"
        "👤 <b>Starring</b>: Macaulay Culkin, Joe Pesci, Daniel Stern\n"
        "🏆 <b>Awards</b>: Nominated for 2 Academy Awards 🏅\n"
        "📖 <b>Plot Summary</b>: 8-year-old Kevin McCallister accidentally gets left behind when his family goes on vacation. "
        "At first, he enjoys his freedom, but when two burglars try to break into his house, Kevin must use clever traps "
        "and tricks to defend his home. A hilarious and heartwarming holiday classic! 🎄\n\n"
        "Do you want to watch it?"
    ))

    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Yes")),
            KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(SectorState.home_alone)
    await message.answer(text, reply_markup=rkb, parse_mode='HTML')


@dp.message(SectorState.home_alone, F.text == __("Yes"))
async def yes_handler_comedy(message: Message, state: FSMContext):
    video_id = "BAACAgIAAxkBAAINLWhwpE_rZ_cvr6VifZoO-aqNWXqqAALkYgAC9XK5SeqQVnNkPDoRNgQ"
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("⬅️ Back")))
    rkb.adjust(1)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await state.set_state(SectorState.yes_hand_comedy)

    await safe_answer_video(
        message,
        video_id=video_id,
        caption=_("🎬 Home Alone (1990)"),
        reply_markup=rkb,
    )

##################################################################################################################
#
# @dp.message(SectorState.comedy_section, F.text == __("🎬 Dumb and Dumber (1994)"))
# async def dump(message: Message, state: FSMContext):
#     text = (_(
#         "🎬 <b>Dumb and Dumber (1994)</b>\n"
#         "⭐ <b>IMDb Rating</b>: 7.3/10\n"
#         "🎭 <b>Genre</b>: Comedy\n"
#         "🎥 <b>Director</b>: Peter Farrelly\n"
#         "👤 <b>Starring</b>: Jim Carrey, Jeff Daniels, Lauren Holly\n"
#         "🏆 <b>Awards</b>: Nominated for 4 MTV Movie Awards 🏅\n"
#         "📖 <b>Plot Summary</b>: Lloyd Christmas and Harry Dunne, two well-meaning but extremely dim-witted "
#         "friends, embark on a hilarious cross-country road trip to return a briefcase full of money to its "
#         "rightful owner. Along the way, their clueless antics and absurd misadventures lead to non-stop "
#         "laughs in this classic comedy. 🤪🚗\n\n"
#         "Do you want to watch it?"
#     ))
#
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("Yes")),
#             KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(2, 1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.dump)
#     await message.answer(text, reply_markup=rkb, parse_mode='HTML')
#
#
# @dp.message(SectorState.dump, F.text == __("Yes"))
# async def yes_handler_dump(message: Message, state: FSMContext):
#     video_id = ""
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.yes_hand_comedy_dump)
#     await message.answer_video(video_id, caption=_("🎬 Dumb and Dumber (1994)"))
#
#
# ##################################################################################################################
#
# @dp.message(SectorState.comedy_section, F.text == __("🎬 The Mask (1994)"))
# async def mask(message: Message, state: FSMContext):
#     text = (_(
#         "🎬 <b>The Mask (1994)</b>\n"
#         "⭐ <b>IMDb Rating</b>: 6.9/10\n"
#         "🎭 <b>Genre</b>: Comedy, Fantasy\n"
#         "🎥 <b>Director</b>: Chuck Russell\n"
#         "👤 <b>Starring</b>: Jim Carrey, Cameron Diaz, Peter Riegert\n"
#         "🏆 <b>Awards</b>: Nominated for 1 Academy Award 🏅\n"
#         "📖 <b>Plot Summary</b>: Stanley Ipkiss, a shy and unlucky bank clerk, stumbles upon a mysterious ancient "
#         "mask that transforms him into a zany, green-faced trickster with extraordinary powers. As he embraces his "
#         "new alter ego, chaos and hilarity ensue, making him the target of both the police and the city's crime boss. "
#         "A wildly entertaining comedy filled with action and over-the-top antics!\n\n"
#         "Do you want to watch it?"
#
#     ))
#
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("Yes")),
#             KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(2, 1)
#
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.mask)
#     await message.answer(text, reply_markup=rkb, parse_mode='HTML')
#
#
# @dp.message(SectorState.mask, F.text == __("Yes"))
# async def yes_handler_dump(message: Message, state: FSMContext):
#     video_id = ""
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.yes_hand_comedy_mask)
#     await message.answer_video(video_id, caption=_("🎬 The Mask (1994)"))
#
#
# ##################################################################################################################
#
# @dp.message(SectorState.comedy_section, F.text == __("🎬 Mrs. Doubtfire (1993)"))
# async def doubtfire(message: Message, state: FSMContext):
#     text = (_(
#         "🎬 <b>The Mask (1994)</b>\n"
#         "⭐ <b>IMDb Rating</b>: 6.9/10\n"
#         "🎭 <b>Genre</b>: Comedy, Fantasy\n"
#         "🎥 <b>Director</b>: Chuck Russell\n"
#         "👤 <b>Starring</b>: Jim Carrey, Cameron Diaz, Peter Riegert\n"
#         "🏆 <b>Awards</b>: Nominated for 1 Academy Award 🏅\n"
#         "📖 <b>Plot Summary</b>: Stanley Ipkiss, a shy and unlucky bank clerk, stumbles upon a mysterious ancient "
#         "mask that transforms him into a zany, green-faced trickster with extraordinary powers. As he embraces his "
#         "new alter ego, chaos and hilarity ensue, making him the target of both the police and the city's crime boss. "
#         "A wildly entertaining comedy filled with action and over-the-top antics!\n\n"
#         "Do you want to watch it?"
#
#     ))
#
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("Yes")),
#             KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(2, 1)
#
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.doubtfire)
#     await message.answer(text, reply_markup=rkb, parse_mode='HTML')
#
#
# @dp.message(SectorState.doubtfire, F.text == __("Yes"))
# async def yes_handler_doubtfire(message: Message, state: FSMContext):
#     video_id = ""
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(KeyboardButton(text=_("⬅️ Back")))
#     rkb.adjust(1)
#     rkb = rkb.as_markup(resize_keyboard=True)
#     await state.set_state(SectorState.yes_hand_comedy_doubtfire)
#     await message.answer_video(video_id, caption=_("🎬 Mrs. Doubtfire (1993)"))
