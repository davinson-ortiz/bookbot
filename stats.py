def count_words(text: str) -> int:
    """Counts the number words in a string."""
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    """Counts the number of occurrences of each character in a string."""
    characters = {}
    for char in text.lower():
        if char == " ":
            continue
        characters[char] = characters.get(char, 0) + 1  
    return characters


def sort_characters(dict_chars: dict) -> list[dict]:
    """Sort characters from the greatest to least by the count"""
    list_of_dicts = [{"char":k, "count":v} for k, v in dict_chars.items()] 
    list_of_dicts.sort(reverse=True, key=lambda x : x["count"])
    return list_of_dicts
