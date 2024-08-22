from aiogram import Router, Dispatcher
from src.common.exceptions import RootRouterParentError
from loguru import logger

__all__ = [
    "RootRouter"
]

class RootRouter(Router):
    def __init__(self, throttling: bool, name: str | None = None) -> None:
        super().__init__(name=name)

        # Проверка на правильного родителя (Dispatcher)
        if self.parent_router is not None and not isinstance(self.parent_router, Dispatcher):
            raise RootRouterParentError("Only Dispatcher can be parent for RootRouter.")

        # Добавляем middlewares
        self._add_catch_exception_middleware()
        self._add_inject_redis_connection_middleware()  # Важно вызвать до следующего метода
        if throttling:
            self._add_set_throttling_middleware()

    def include_router(self, router: Router) -> None:
        # Проверка перед добавлением роутера
        if router.parent_router is None:
            super().include_router(router)
        else:
            logger.warning(f"Router '{router.name}' is already attached.")

    def _add_catch_exception_middleware(self) -> None:
        pass

    def _add_set_throttling_middleware(self) -> None:
        pass

    def _add_inject_redis_connection_middleware(self) -> None:
        pass
