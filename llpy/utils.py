from typing import Callable

from . import mc


def listen(event: str):
    """
    监听事件函数装饰器

    Args:
        event: 要监听的事件名称
    """

    def wrapper(func: Callable[..., bool | None]):
        mc.listen(event, func)
        return func

    return wrapper
