from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const

from tgbot.states.main_menu import MainMenu

main_menu_dialog = Dialog(
    Window(
        Const('Привет!'),
        Const('Используй /analyze для анализа присланного текста'),
        Const('Доступ к Notion - /notion'),
        state=MainMenu.main_menu
    )

)
