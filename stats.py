def get_book_text(filepath):
    with open(filepath, encoding="utf-8-sig") as f:
        file_content = f.read()
    return file_content

def count_characters(input_string, dict_of_chars):
    for character in input_string:
        lower = character.lower()
        if not lower in dict_of_chars:
            dict_of_chars[lower] = 1
        else:
            dict_of_chars[lower] += 1
    return dict_of_chars

def sort_on(items):
    return items["num"]

def dict_transform(dictionary):
    list_of_dict = []
    for item in dictionary:
        value = dictionary[item]
        formatted_value = {"char": item, "num": value}
        list_of_dict.append(formatted_value)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
