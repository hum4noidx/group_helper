from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from pydantic import parse_obj_as

from tgbot.models.text_analyze import TextAnalysis
from tgbot.utils.analyze_text import make_analysis

analysis_router = Router()


class AnalyzeText(StatesGroup):
    enter_text = State()


@analysis_router.message(Command(commands='analyze'))
async def analyze_text_handler(event: Message, state: FSMContext):
    await event.reply('Пришли мне текст, чтобы я его проанализировал\n'
                      'Я не сохраняю эти данные!')
    await state.set_state(AnalyzeText.enter_text)


@analysis_router.message(AnalyzeText.enter_text)
async def analyze_text(event: Message, state: FSMContext):
    await state.clear()
    text = event.html_text
    if not text:
        await event.reply('Я принимаю только текстовые сообщения!')
        return
    analysis: TextAnalysis = parse_obj_as(TextAnalysis, make_analysis(text))
    await event.reply(f'<b>Стастистика по тексту:</b>\n'
                      f'<b>Предложений:</b> {analysis.sentences}\n'
                      f'<b>Символов:</b> {analysis.characters}\n'
                      f'<b>Абзацев:</b> {analysis.paragraphs}\n\n'

                      f'<b>Уникальных слов:</b> {analysis.unique_words}\n'
                      f'<b>Слов в предложении:</b> {analysis.words_per_sentence}\n'
                      f'<b>Предлогов:</b> {analysis.prepositions}\n'
                      f'<b>Местоимений:</b> {analysis.articles}\n'
                      f'<b>Букв в предложении:</b> {analysis.letters_per_sentence}\n'
                      f'<b>Слогов в слове:</b> {analysis.syllables_per_word}\n'
                      f'<b>Букв всего:</b> {analysis.letters_total}\n'
                      f'<b>Страниц:</b> {analysis.printed_pages}\n'
                      f'<b>Слов между запятыми:</b> {analysis.words_between_pauses}\n'
                      f'<b>Запятых в предложении:</b> {analysis.pauses_per_sentence}\n'
                      f'<b>Максимальная длина предложения:</b> {analysis.max_sentence_length}\n'
                      f'<b>Вопросительных предложений:</b> {analysis.questions}\n'
                      f'<b>Букв в слове:</b> {analysis.letters_per_word}\n'
                      f'<b>Буквенно-цифровых символов:</b> {analysis.alphanumeric_characters}\n'
                      f'<b>Слов в абзаце:</b> {analysis.words_per_paragraph}\n'
                      f'<b>Слогов в предложении:</b> {analysis.syllables_per_sentence}\n'
                      f'<b>Слогов всего:</b> {analysis.syllables_total}\n'
                      f'<b>Слов всего:</b> {analysis.words_total}\n'
                      f'<b>Запятых:</b> {analysis.pauses}\n'
                      f'<b>Местоимений:</b> {analysis.pronouns}\n'
                      f'<b>Первое лицо:</b> {analysis.first_person}\n'
                      f'<b>Второе лицо:</b> {analysis.second_person}\n'
                      f'<b>Третье лицо:</b> {analysis.third_person}\n'
                      )
