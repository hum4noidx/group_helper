import datetime

from aiogram import Router
from aiogram.filters import Command, CommandObject, StateFilter
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from infrastructure.database.repositories.user import UserRepo
from tgbot.handlers.group.important_notes import add_msg_to_important_thread
from tgbot.states.main_menu import MainMenu
from tgbot.utils.system_config import getsysteminfo


async def configuration(event: Message):
    config_info = getsysteminfo()
    await event.reply(f'<b>Current server configuration:</b>\n'
                      f'<b>Platform:</b> {config_info["platform"]}\n'
                      f'<b>Release:</b> {config_info["platform-release"]}\n'
                      f'<b>Platform version:</b> {config_info["platform-version"]}\n'
                      f'<b>Architecture:</b> {config_info["architecture"]}\n'
                      f'<b>Processor:</b> {config_info["processor"]}\n'
                      f'<b>RAM:</b> {config_info["ram"]}\n'
                      f'<b>Python version:</b> {config_info["python"]}\n')


async def get_info(event: Message):
    await event.reply('Бот для управления группой и еще чем-то\n'
                      'Source code: https://github.com/hum4noidx/group_helper\n'
                      'Отправить сообщение в важный чат: !i \n'
                      'Выдать мут: !ro 1m \n'
                      )


async def start(event: Message, dialog_manager: DialogManager, user_repo: UserRepo, command: CommandObject):
    # if command args needed e.g. /start 123 wil return 123
    # args = command.args
    await user_repo.update_user_if_not_exists(event.from_user.id, event.from_user.full_name, datetime.datetime.now())
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def get_id(event: Message):
    await event.reply(f'Ваш ID: <code>{event.from_user.id}</code>\n')


def register_user_router(router: Router):
    router.message.register(start, Command(commands='start'), StateFilter('*'))
    router.message.register(configuration, Command(commands=['config']), StateFilter('*'))
    router.message.register(get_id, Command(commands=['id']), StateFilter('*'))
    router.message.register(add_msg_to_important_thread, Command(commands='i', prefix='!'), StateFilter('*'))
    router.message.register(get_info, Command(commands=['info']), StateFilter('*'))
