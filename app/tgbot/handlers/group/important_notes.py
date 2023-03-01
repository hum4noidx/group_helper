import logging

from aiogram import Bot
from aiogram.types import Message

logger = logging.getLogger(__name__)


async def add_msg_to_important_thread(event: Message, bot: Bot):
    if event.reply_to_message:
        logger.info(f'User {event.from_user.id}|{event.from_user.full_name} added message to important thread')
        await event.reply_to_message.forward(chat_id=event.chat.id, message_thread_id=4578)
    else:
        logger.info(f'User {event.from_user.id}|{event.from_user.full_name} added message to important thread')
        await event.forward(chat_id=event.chat.id, message_thread_id=4578)
    await event.reply('✅ Сообщение добавлено в важную тему')
