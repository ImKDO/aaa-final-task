import pytest

from dto_pizza import Margherita
from kitchen import bake, delivery, pickup


def test_bake(capsys: pytest.CaptureFixture[str]) -> None:
    pizza = Margherita()
    result = bake(pizza)

    assert result is pizza
    assert "Приготовили за" in capsys.readouterr().out


def test_delivery(capsys: pytest.CaptureFixture[str]) -> None:
    pizza = Margherita()
    result = delivery(pizza)

    assert result is pizza
    assert "Доставили за" in capsys.readouterr().out


def test_pickup(capsys: pytest.CaptureFixture[str]) -> None:
    pizza = Margherita()
    result = pickup(pizza)

    assert result is pizza
    assert "Забрали за" in capsys.readouterr().out
