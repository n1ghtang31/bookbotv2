from stats import split_text, count_characters, split_char, generate_report

def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def main(path):
    text = get_book_text(path)
    count = count_characters(text)
    print(generate_report(text, path))
    
book = "books/frankenstein.txt"
text = get_book_text(book)
main(book)
