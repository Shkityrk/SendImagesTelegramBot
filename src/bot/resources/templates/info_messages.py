__all__ = [
    "START_COMMAND_TEMPLATE",
    "SET_SEARCH_MESSAGE",
    "SET_SEARCH_MESSAGE_SUCCESS",
    "GET_SEARCH_MESSAGE_SUCCESS",
    "GET_SEARCH_MESSAGE_ERROR",
    "SET_SLEEP_TIME_MESSAGE",
    "SET_SLEEP_TIME_MESSAGE_SUCCESS",
    "SET_SLEEP_TIME_MESSAGE_ERROR_ISNULL",
    "SET_SLEEP_TIME_MESSAGE_ERROR_ISDIGIT",
    "SET_SLEEP_TIME_MESSAGE_ERROR_ISNATURAL",
    "SEND_IMAGE_NULL_PROMPT",
    "STOP_SEND_IMAGE_SUCCESS",
    "STOP_SEND_IMAGE_NULL",
]

START_COMMAND_TEMPLATE = """<b>Привет!</b>
Бот запущен. Введите /help для получения списка доступных команд"""

SET_SEARCH_MESSAGE = """Пожалуйста, введите фразу для поиска"""

SET_SEARCH_MESSAGE_SUCCESS = """Поисковый запрос установлен: """

GET_SEARCH_MESSAGE_SUCCESS = """Выбранный поисковый запрос: """
GET_SEARCH_MESSAGE_ERROR = """Вы не установили поисковый запрос. Введите <i>/set_search</i> для установки."""

# set_sleep_time
SET_SLEEP_TIME_MESSAGE = """Введите целочисленное значение задержки, в секундах"""
SET_SLEEP_TIME_MESSAGE_SUCCESS = """Установлено значение: """
SET_SLEEP_TIME_MESSAGE_ERROR_ISNULL = """Пожалуйста, введите целое число для времени задержки."""
SET_SLEEP_TIME_MESSAGE_ERROR_ISDIGIT = """Ошибка: Введите положительное целое число."""
SET_SLEEP_TIME_MESSAGE_ERROR_ISNATURAL = """Ошибка: Время задержки должно быть больше нуля."""

SEND_IMAGE_NULL_PROMPT = """Поисковый запрос не установлен. Используйте команду /set_search для его установки."""

STOP_SEND_IMAGE_SUCCESS = """Отправка изображений остановлена."""
STOP_SEND_IMAGE_NULL = """Никакие изображения не отправляются в данный момент."""
