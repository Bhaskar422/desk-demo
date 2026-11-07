from textkit import char_count, title_case, word_count


def test_word_count():
    assert word_count("hello there") == 2


def test_title_case():
    assert title_case("hello there") == "Hello There"


def test_char_count_includes_whitespace_by_default():
    assert char_count("hello big world") == 15


def test_char_count_skip_spaces():
    assert char_count("hello big world", spaces=False) == 13


def test_char_count_skip_all_whitespace():
    assert char_count("a\tb\nc  ", spaces=False) == 3


def test_char_count_empty():
    assert char_count("") == 0
    assert char_count("   ", spaces=False) == 0
