from stats import (
    get_book_character_count,
    get_book_word_count,
    get_report,
    sort_character_dicts,
)


def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_book_word_count(book_text)
    char_count = get_book_character_count(book_text)
    sorted_char_count = sort_character_dicts(char_count)
    report = get_report(file_path, word_count, sorted_char_count)
    print(report)
    # print(sorted_char_count)


if __name__ == "__main__":
    main()
