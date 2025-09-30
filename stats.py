def get_num_words(text:str) -> int:
    words = text.split()
    count = len(words)
    return count

def get_character_count(text:str) -> dict:
    character_dict = {}
    for c in text.lower():
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1

    return character_dict