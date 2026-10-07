from dto_pizza import Hawaiian, Margherita, Pepperoni, Pizza, Size


def test_default_size() -> None:
    pizza = Margherita()
    assert pizza.size == Size.L


def test_xl_size() -> None:
    pizza = Pepperoni(Size.XL)
    assert pizza.size == Size.XL


def test_name() -> None:
    assert Margherita().name == "Margherita"
    assert Pepperoni().name == "Pepperoni"
    assert Hawaiian().name == "Hawaiian"


def test_margherita_ingredients() -> None:
    assert Margherita().ingredients == ["tomato sauce", "mozzarella", "tomatoes"]


def test_pepperoni_ingredients() -> None:
    assert Pepperoni().ingredients == ["tomato sauce", "mozzarella", "pepperoni"]


def test_hawaiian_ingredients() -> None:
    assert Hawaiian().ingredients == [
        "tomato sauce",
        "mozzarella",
        "chicken",
        "pineapples",
    ]


def test_dict() -> None:
    pizza = Hawaiian(Size.XL)
    assert pizza.dict() == {
        "size": "XL",
        "sauce": "tomato sauce",
        "cheese": "mozzarella",
        "other": ["chicken", "pineapples"],
    }


def test_equal_pizzas() -> None:
    assert Pepperoni() == Pepperoni()


def test_different_size_not_equal() -> None:
    assert Pepperoni(Size.L) != Pepperoni(Size.XL)


def test_different_pizzas_not_equal() -> None:
    assert Margherita() != Hawaiian()


def test_pizza_not_equal_to_string() -> None:
    assert Pizza() != "pizza"


def test_repr() -> None:
    assert "Margherita" in repr(Margherita())
