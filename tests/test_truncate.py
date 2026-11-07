import pytest

from textkit.core import truncate


def test_short_text_is_unchanged():
    assert truncate("hi", 10) == "hi"


def test_long_text_is_cut_with_ellipsis():
    assert truncate("hello there world", 9) == "hello th…"


def test_width_must_fit_ellipsis():
    with pytest.raises(ValueError):
        truncate("hello", 0)
