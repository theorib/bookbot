from typing import List


def get_book_word_count(book_text: str) -> int:
    return len(book_text.split())


def get_book_character_count(book_text: str) -> dict[str, int]:
    book_text_lower = book_text.lower()

    result = {}

    for char in book_text_lower:
        if char in result:
            continue
        result[char] = book_text_lower.count(char)

    return result


def sort_character_dicts(character_count: dict[str, int]) -> List[dict[str, dict]]:
    # {new_key:new_value for (key, value) ‹dict ›.items ()if ‹condition›}
    dicts = [{"char": char, "num": count} for (char, count) in character_count.items()]
    dicts.sort(key=lambda char: char["num"], reverse=True)
    return dicts


def get_report(file_path: str, word_count: int, character_dicts: list) -> str:
    report = f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{"".join([f"{d['char']}: {d['num']}\n" for d in character_dicts if d["char"].isalpha()])}============= END ===============
"""
    return report
