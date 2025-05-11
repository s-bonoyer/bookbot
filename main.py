import sys
from stats import num_words, dict_sort

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
count = num_words(path)
full_dict = dict_sort(path)
def report(count, dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in dict:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

report(count, full_dict)