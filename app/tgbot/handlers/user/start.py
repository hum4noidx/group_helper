import datetime

from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram_dialog import DialogManager, StartMode

from configreader import config
from infrastructure.database.repositories.user import UserRepo
from tgbot.states.main_menu import MainMenu


async def start(m: Message, dialog_manager: DialogManager, user_repo: UserRepo, command: CommandObject):
    # if command args needed e.g. /start 123 wil return 123
    # args = command.args
    await user_repo.update_user_if_not_exists(m.from_user.id, m.from_user.full_name, datetime.datetime.now())
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def get_id(m: Message):
    await m.reply(f'Ваш ID: <code>{m.from_user.id}</code>\n')


async def open_notion(event: Message, bot: Bot):
    await message.answer(
        "Notion's here!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Open Webview", web_app=WebAppInfo(url=f"{config.webhook_domain}/notion")
                    )
                ]
            ]
        ),
    )


def register_user_router(router: Router):
    router.message.register(start, Command(commands='start'))
    router.message.register(get_id, Command(commands=['id']))
    router.message.register(open_notion, Command(commands=['notion']))
