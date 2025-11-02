def split_text(text):
    split = text.split()
    num_words = len(split)
    print(f"Found {num_words} total words")
    return split

def split_char(text):
    split_char = text.split()
    return split_char

def count_characters(text):
    characters = {}

    for char in text:
        char_low = char.lower()
        if char_low in characters:
            characters[char_low] += 1
        else:
            characters[char_low] = 1
    return characters
