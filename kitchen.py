"""Этапы выполнения заказа: готовка, доставка и самовывоз."""

from decorators import log
from dto_pizza import Pizza


@log("👩‍🍳 Приготовили за {}с!")
def bake(pizza: Pizza) -> Pizza:
    """Готовит пиццу."""
    return pizza


@log("🛵 Доставили за {}с!")
def delivery(pizza: Pizza) -> Pizza:
    """Доставляет пиццу."""
    return pizza


@log("🏠 Забрали за {}с!")
def pickup(pizza: Pizza) -> Pizza:
    """Самовывоз."""
    return pizza
