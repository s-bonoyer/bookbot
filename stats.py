def get_book_text(path):
    with open(path) as book:
        return book.read()

def num_words():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    book_words = text.split()
    words_total = len(book_words)
    print(f"{words_total} words found in the document")

def num_chars():
    char_count = {}
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    lowers = text.lower()
    all_words = lowers.split()
    for word in all_words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count