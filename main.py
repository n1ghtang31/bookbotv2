from stats import split_text, count_characters, split_char

def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def main(path):
    print(get_book_text(path))

book = "books/frankenstein.txt"
# main(book)

