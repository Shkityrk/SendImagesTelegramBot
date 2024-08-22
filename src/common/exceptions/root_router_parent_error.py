__all__ = [
    "RootRouterParentError"
]


class RootRouterParentError(Exception):
    """Raise if parent of RootRouter is not a Dispatcher"""
