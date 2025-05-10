def get_book_text(path):
    with open(path) as book:
        return book.read()

def num_words():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    book_words = text.split()
    words_total = len(book_words)
    return words_total

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

def dict_sort():
    alpha_dict = []
    dict = num_chars()
    for entry in dict:
        if entry.isalpha() == True:
            char_dict = {"char": entry, "num": dict[entry]}
            alpha_dict.append(char_dict)
    
    alpha_dict.sort(reverse=True, key=lambda check: check["num"])
    return alpha_dict