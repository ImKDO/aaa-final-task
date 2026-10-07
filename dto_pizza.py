"""Рецепты пицц"""

from enum import StrEnum

type Recipe = dict[str, str | list[str]]


class Size(StrEnum):
    """Доступные размеры пиццы."""

    L = "L"
    XL = "XL"


class Pizza:
    """Базовый рецепт пиццы: соус, сыр и остальные начинки.

    Конкретные пиццы переопределяют атрибуты класса с рецептом.
    """

    icon: str = "🍕"
    sauce: str = "tomato sauce"
    cheese: str = "mozzarella"
    other: tuple[str, ...] = ()

    def __init__(self, size: Size = Size.L) -> None:
        self.size: Size = size

    @property
    def name(self) -> str:
        """Название пиццы для меню."""
        return type(self).__name__

    @property
    def ingredients(self) -> list[str]:
        """Все ингредиенты рецепта по порядку."""
        return [self.sauce, self.cheese, *self.other]

    def __eq__(self, other: object) -> bool:
        """Пиццы равны, если у них одинаковые размер и рецепт."""
        if not isinstance(other, Pizza):
            return NotImplemented
        return all(
            (
                self.size == other.size,
                self.sauce == other.sauce,
                self.cheese == other.cheese,
                self.other == other.other,
            )
        )

    def __repr__(self) -> str:
        return f"{self.name}(size={self.size!r})"

    def dict(self) -> Recipe:
        """Рецепт в виде словаря."""
        return {
            "size": str(self.size),
            "sauce": self.sauce,
            "cheese": self.cheese,
            "other": list(self.other),
        }


class Margherita(Pizza):
    icon = "🧀"
    other = ("tomatoes",)


class Pepperoni(Pizza):
    icon = "🍕"
    other = ("pepperoni",)


class Hawaiian(Pizza):
    icon = "🍍"
    other = ("chicken", "pineapples")
