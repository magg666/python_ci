
def make_new_string(word: str):
    try:
        new_word = word[::-1]
    except TypeError as e:
        return e
    else:
        return new_word

