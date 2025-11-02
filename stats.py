def split_text(text):
    split = text.split()
    num_words = len(split)
    # print(f"Found {num_words} total words")
    return num_words

def split_char(text):
    split_char = text.split()
    return split_char

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    result = []

    for char in char_counts:
        count = char_counts[char]
        result.append({"char": char, "num": count})
    
    return result


def sort_report(text):
    return text["num"]

def generate_report(text, path):
    words = split_text(text)
    count = count_characters(text)
    count.sort(reverse=True, key=sort_report)
    
    string_report = f"""=================== BOOKBOT ====================\n
Analyzing book found at {path}...\n
---------- Word Count ------------\n
Found {words} total words\n
---------- Character Count -------\n
"""
    for char in count:
        string_report = string_report + f"{char['char']}: {char['num']}\n"
    return string_report

