from stats import count_words, count_characters, sort_List, nice_print
import sys


def get_book_text():
    with open(sys.argv[1]) as f:
        file_content = f.read()
        return file_content


def checkArg():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    # print(get_book_text())
    checkArg()
    print(count_words(get_book_text()))
    # print(count_characters((get_book_text())))
    sorted_dictionary = sort_List(count_characters(get_book_text()))
    nice_print(sorted_dictionary)


main()
