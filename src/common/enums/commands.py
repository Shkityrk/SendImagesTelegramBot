from enum import StrEnum, unique

__all__ = [
    "TelegramCommand"
]


@unique
class TelegramCommand(StrEnum):
    """Telegram commands for filters to handlers"""
    START_COMMAND = "start"
    SET_SEARCH_COMMAND = "set_search"
    GET_SEARCH_COMMAND = "get_search"
    SEND_IMAGE_COMMAND = "send_images"
    STOP_IMAGE_COMMAND = "stop_images"
    HELP_COMMAND = "help"
    SET_SLEEP_TIME = "set_sleep_time"
