def main():
    content = get_book_text("books/frankenstein.txt")
    print(count_words(content))

def count_words(content):
    words = content.split()
    return f"{len(words)} words found in the document"

def get_book_text(path_to_file):
    content = ""
    with open(path_to_file) as f:
       content = f.read()
    return content



main()
