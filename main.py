import sys
from stats import get_num_words, get_character_count, sort_dict

def get_book_text(filepath:str) -> str:
    """
    Takes filepath and returns text
    """
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def main():
    if sys.argv.count == 1:
        print("Error: No argument given")
        print("example: main.py books/frankenstein.txt")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_dict(get_character_count(text)):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
