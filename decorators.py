"""Декоратор, логирующий имя функции и время её выполнения."""

from collections.abc import Callable
from functools import wraps
from random import randint
from typing import overload

DEFAULT_TEMPLATE = "{name} — {}с!"


@overload
def log[**P, R](template: Callable[P, R]) -> Callable[P, R]: ...


@overload
def log[**P, R](
    template: str = DEFAULT_TEMPLATE,
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...


def log[**P, R](
    template: str | Callable[P, R] = DEFAULT_TEMPLATE,
) -> Callable[P, R] | Callable[[Callable[P, R]], Callable[P, R]]:
    """Выводит имя функции и время выполнения (случайное, через randint).

    Можно использовать без аргументов — ``@log`` выведет ``'bake — 2с!'``,
    или с шаблоном — ``@log('Доставили за {}с!')``. В шаблон вместо ``{}``
    подставляется время, вместо ``{name}`` — имя функции.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)
            elapsed = randint(1, 5)
            print(fmt.format(elapsed, name=func.__name__))
            return result

        return wrapper

    if callable(template):
        fmt = DEFAULT_TEMPLATE
        return decorator(template)
    fmt = template
    return decorator
