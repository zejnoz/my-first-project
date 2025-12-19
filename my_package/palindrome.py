def is_palidrome(word: str) -> bool:
    lower_word = word.lower()
    return lower_word == lower_word[::-1]
