from aiogram.types import Message

from domain.dto.bad_words import BadWordDTO
from infrastructure.database.repositories.bot import BotRepo


async def filter_bad_words(m: Message, bot_repo: BotRepo):
    bad_words: BadWordDTO = await bot_repo.get_bad_words()
    for word in bad_words.word:
        if word in m.text:
            await m.delete()
            await m.answer('Не матерись!')
            return
