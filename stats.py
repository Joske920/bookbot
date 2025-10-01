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

def sort_dict(char_dict:dict) -> list:
    """
    Takes a dictionary of characters and their counts,
    returns a sorted list of dictionaries in descending order of counts.
    """
    # Convert {char: count} into [{"char": char, "num": count}, ...]
    char_list = [{"char": c, "num": n} for c, n in char_dict.items()]
    
    # Helper function for sorting
    def get_num(entry):
        return entry["num"]
    
    # Sort in-place, from greatest to least
    char_list.sort(key=get_num, reverse=True)
    
    return char_list