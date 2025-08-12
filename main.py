from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    words_count = get_num_words(content)
    print(f"{words_count} words found in the document")
    


def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return f.read()



main()
