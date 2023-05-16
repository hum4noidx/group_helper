import logging
from datetime import datetime

from aiogram import Bot, types, exceptions
from aiogram.types import ChatPermissions

from tgbot.utils.timedelta import parse_timedelta_from_message

logger = logging.getLogger(__name__)


async def cmd_ro(event: types.Message, bot: Bot):
    duration = await parse_timedelta_from_message(event)
    if not duration:
        return

    try:  # Apply restriction
        await bot.restrict_chat_member(
            chat_id=event.chat.id, user_id=event.reply_to_message.from_user.id, permissions=ChatPermissions(
                can_send_messages=False,
            ), until_date=duration
        )
        user = event.reply_to_message.from_user.id
        admin = event.from_user.id
        duration = duration
        logger.info(
            f"User {user} restricted by {admin} for {duration}",
            extra={"user": user, "admin": admin, "duration": duration})

    except exceptions.TelegramBadRequest as e:
        logger.error(f"Failed to restrict chat member: {e}", exc_info=True)
        return False
    ro_until = datetime.now() + duration
    await event.reply_to_message.reply(
        f'🤫 Read-only mode enabled until {ro_until.strftime("%H:%M:%S %d.%m.%Y")}')
    return True
