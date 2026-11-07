"""Small text helpers."""
import re


def word_count(text: str) -> int:
    """Count the words in text."""
    return len(re.findall(r"[A-Za-z0-9]+", text))


def title_case(text: str) -> str:
    """Capitalise the first letter of every word."""
    return re.sub(r"[A-Za-z]+", lambda m: m.group(0).capitalize(), text)


def char_count(text: str, spaces: bool = True) -> int:
    """Count the characters in ``text``.

    When ``spaces`` is False, whitespace characters (spaces, tabs, newlines,
    etc.) are excluded from the count.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if spaces:
        return len(text)
    return sum(1 for char in text if not char.isspace())
