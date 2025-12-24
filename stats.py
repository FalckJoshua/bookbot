def count_words(book: str):
    count = 0
    word_list = book.split()
    for word in word_list:
        count += 1
    return f"Found {count} total words"


def count_characters(book: str):
    book = book.lower()
    characters = {}
    for letter in book:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters


def sort_on(item):
    return item["num"]


def nice_print(dictionary: dict):
    for dict in dictionary:
        print(f"{dict}: {dictionary[dict]}")


def sort_List(characters: dict):
    dict_list = []
    for char in characters:
        if char.isalpha():
            temp = {"char": char, "num": characters[char]}
            dict_list.append(temp)
    dict_list.sort(reverse=True, key=sort_on)
    sorted_dict = {}
    for dic in dict_list:
        sorted_dict[dic["char"]] = dic["num"]

    return sorted_dict
