import pytest

from decorators import log


def test_log_without_args(capsys: pytest.CaptureFixture[str]) -> None:
    @log
    def foo() -> int:
        return 42

    result = foo()
    output = capsys.readouterr().out

    assert result == 42
    assert "foo" in output
    assert "с!" in output


def test_log_with_template(capsys: pytest.CaptureFixture[str]) -> None:
    @log("Готово за {}с!")
    def bar() -> str:
        return "ok"

    result = bar()
    output = capsys.readouterr().out

    assert result == "ok"
    assert output.startswith("Готово за ")


def test_log_with_name_in_template(capsys: pytest.CaptureFixture[str]) -> None:
    @log("{name} отработала за {}с")
    def baz() -> None:
        pass

    baz()
    output = capsys.readouterr().out

    assert "baz отработала" in output


def test_log_passes_arguments() -> None:
    @log
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5


def test_log_keeps_function_name() -> None:
    @log
    def my_func() -> None:
        pass

    assert my_func.__name__ == "my_func"


def test_time_is_from_1_to_5(capsys: pytest.CaptureFixture[str]) -> None:
    @log("{}")
    def func() -> None:
        pass

    for _ in range(20):
        func()
        output = capsys.readouterr().out
        assert 1 <= int(output) <= 5
