from src.bot.root import RootRouter
from src.bot.controllers.messages import (
    include_help_command_router,
    include_start_command_router,
    include_set_search_command_router,
    include_get_search_command_router,
    include_send_img_command_router,
    include_stop_images_command_router,
    include_set_sleep_time_command_router,
)


__all__ = [
    "build_root_router"
]


def build_root_router() -> RootRouter:
    THROTTLING = True
    root_router = RootRouter(THROTTLING)

    include_start_command_router(root_router)
    include_help_command_router(root_router)
    include_set_search_command_router(root_router)
    include_get_search_command_router(root_router)
    include_send_img_command_router(root_router)
    include_stop_images_command_router(root_router)
    include_set_sleep_time_command_router(root_router)

    return root_router
