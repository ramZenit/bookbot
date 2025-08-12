def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_chars(content):
    chars = {}
    for char in content.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars