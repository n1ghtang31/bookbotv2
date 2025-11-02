from stats import split_text, count_characters, split_char, generate_report
import sys


def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def main(path):
    text = get_book_text(path)
    count = count_characters(text)
    print(generate_report(text, path))


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


book = sys.argv[1]
main(book)

