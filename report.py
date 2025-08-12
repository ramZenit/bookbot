def print_report(book_path, words_count, dict_list):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {book_path}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {words_count} total words\n"
    report += "--------- Character Count -------\n"
    for dict in dict_list:
        if dict["char"].isalpha():
            report += f"{dict["char"]}: {dict["num"]}\n"
    report += "============= END ==============="
    print(report)