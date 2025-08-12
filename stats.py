def get_num_words(content):
    words_list = content.split()
    return len(words_list)

def get_chars_dict(content):
    chars_dict = {}
    for char in content.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def create_dict_list(chars_dict):
    dict_list = []
    for char in chars_dict:
        dict = {
            "char": char,
            "num": chars_dict[char]
        }
        dict_list.append(dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]