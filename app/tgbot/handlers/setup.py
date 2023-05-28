import logging

from aiogram import Dispatcher, Router, F
from aiogram_dialog import DialogRegistry

from tgbot.handlers.admin import admin
from tgbot.handlers.user import main_menu, start
from tgbot.handlers.user.analyze import analysis_router
from tgbot.middlewares.db import DbSessionMiddleware
from tgbot.middlewares.deny_access import AccessMiddleware
from tgbot.middlewares.maintenance import MaintenanceMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware

logger = logging.getLogger(__name__)


def register_middlewares(dp: Dispatcher, db_pool):
    dp.message.outer_middleware(DbSessionMiddleware(db_pool))
    dp.message.middleware(DbSessionMiddleware(db_pool))
    dp.callback_query.middleware(DbSessionMiddleware(db_pool))
    dp.inline_query.middleware(DbSessionMiddleware(db_pool))
    dp.message.middleware(MaintenanceMiddleware())
    dp.callback_query.middleware(MaintenanceMiddleware())
    dp.message.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(ThrottlingMiddleware())
    dp.message.middleware(AccessMiddleware())
    dp.callback_query.middleware(AccessMiddleware())
    logger.info('Middlewares successfully registered')


def register_dialogs(dp: Dispatcher):
    dialog_registry = DialogRegistry(dp)

    # ========= User dialogs =========
    dialog_registry.register(main_menu.main_menu_dialog)
    logger.info('Dialogs successfully registered')
    return dialog_registry


def register_handlers(dp: Dispatcher):
    dialogs_router = Router()
    dialogs_router.message.filter(F.chat.type == "private")

    dp.include_router(admin.setup())
    dp.include_router(analysis_router)
    dp.include_router(start.setup())
    dp.include_router(dialogs_router)
    registry: DialogRegistry = register_dialogs(dp)
    logger.info('Handlers successfully registered')
    return registry
