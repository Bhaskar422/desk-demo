from textkit import char_count, title_case, word_count


def test_char_count():
    assert char_count("a b") == 3
    assert char_count("a b", spaces=False) == 2


def test_word_count():
    assert word_count("hello there") == 2


def test_title_case():
    assert title_case("hello there") == "Hello There"
