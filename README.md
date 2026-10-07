# aaa-final-task

## Структура

- `dto_pizza.py` — рецепты (`Margherita`, `Pepperoni`, `Hawaiian`), размеры `L`/`XL`, `dict()` и `__eq__`
- `decorators.py` — декоратор `log` (`@log` или `@log("шаблон {}с!")`)
- `kitchen.py` — этапы заказа: `bake`, `delivery`, `pickup`
- `main.py` — команды `menu` и `order`
- `tests/` — тесты на pytest

## Запуск

```bash
uv sync
uv run python main.py menu
uv run python main.py order pepperoni --delivery
uv run python main.py order hawaiian --size XL
```