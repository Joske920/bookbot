from stats import get_num_words, get_character_count

def get_book_text(filepath:str) -> str:
    """
    Takes filepath and returns text
    """
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def main():
    text = get_book_text(r"books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print(get_character_count(text))

main()
