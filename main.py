from stats import num_words, dict_sort
count = num_words()
full_dict = dict_sort()
def report(count, dict):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in dict:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

report(count, full_dict)