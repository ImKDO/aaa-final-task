import click

from dto_pizza import Hawaiian, Margherita, Pepperoni, Pizza, Size
from kitchen import bake, delivery, pickup

PIZZA_MENU: dict[str, type[Pizza]] = {
    "margherita": Margherita,
    "pepperoni": Pepperoni,
    "hawaiian": Hawaiian,
}


@click.group()
def cli() -> None:
    """Инициализация консольного приложения"""


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza_cls in PIZZA_MENU.values():
        pizza = pizza_cls()
        ingredients = ", ".join(pizza.ingredients)
        click.echo(f"- {pizza.name} {pizza.icon}: {ingredients}")


@cli.command()
@click.argument(
    "pizza_type",
    type=click.Choice(list(PIZZA_MENU), case_sensitive=False),
)
@click.option(
    "--size",
    default=Size.L.value,
    type=click.Choice([size.value for size in Size], case_sensitive=False),
    help="Размер пиццы",
)
@click.option("--delivery", "is_delivery", is_flag=True, help="Включить доставку")
def order(pizza_type: str, size: str, is_delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    pizza = PIZZA_MENU[pizza_type.lower()](Size(size.upper()))
    bake(pizza)
    if is_delivery:
        delivery(pizza)
    else:
        pickup(pizza)


if __name__ == "__main__":
    cli()
