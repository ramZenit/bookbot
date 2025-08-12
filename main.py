from stats import get_num_words
from stats import get_num_chars

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    words_count = get_num_words(content)
    print(f"{words_count} words found in the document")
    chars_count = get_num_chars(content)
    print(chars_count)
    #for char in chars_count:
        #print(f"'{char}': {chars_count[char]}")
    
    


def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()



main()
