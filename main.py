def get_book_text(filepath:str) -> str:
    """
    Takes filepath and returns text
    """
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def main():
    print(get_book_text(r"books/frankenstein.txt"))


main()
