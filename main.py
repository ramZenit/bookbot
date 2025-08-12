def main():
    content = get_book_text("books/frankenstein.txt")
    print(content)








def get_book_text(path_to_file):
    content = ""
    with open(path_to_file) as f:
       content = f.read()
    return content



main()
