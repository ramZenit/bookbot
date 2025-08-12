from stats import get_num_words
from stats import get_chars_dict
from stats import create_dict_list
from report import print_report

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    words_count = get_num_words(content)
    chars_dict = get_chars_dict(content)
    dict_list = create_dict_list(chars_dict)
    print_report(book_path, words_count, dict_list)
    


def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()



main()
