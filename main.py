from stats import get_num_words
from stats import get_chars_dict
from stats import create_dict_list
from report import print_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    words_count = get_num_words(content)
    chars_dict = get_chars_dict(content)
    dict_list = create_dict_list(chars_dict)
    print_report(book_path, words_count, dict_list)
    


def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file '{path_to_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


main()
