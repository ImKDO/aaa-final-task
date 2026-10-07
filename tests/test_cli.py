from click.testing import CliRunner

from main import cli


def test_menu() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["menu"])

    assert result.exit_code == 0
    assert "Margherita" in result.output
    assert "Pepperoni" in result.output
    assert "Hawaiian" in result.output


def test_order_pickup() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni"])

    assert result.exit_code == 0
    assert "Приготовили" in result.output
    assert "Забрали" in result.output
    assert "Доставили" not in result.output


def test_order_delivery() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni", "--delivery"])

    assert result.exit_code == 0
    assert "Приготовили" in result.output
    assert "Доставили" in result.output
    assert "Забрали" not in result.output


def test_order_xl() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "hawaiian", "--size", "XL"])

    assert result.exit_code == 0


def test_order_uppercase() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "MARGHERITA", "--size", "xl"])

    assert result.exit_code == 0


def test_order_unknown_pizza() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "calzone"])

    assert result.exit_code != 0


def test_order_wrong_size() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni", "--size", "M"])

    assert result.exit_code != 0
