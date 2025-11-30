import sys
from stats import get_book_text, count_characters, dict_transform
characters_dict = {}

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    books = get_book_text(sys.argv[1])
    counter = count_characters(books, characters_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {len(books.split())} total words")
    print(f"--------- Character Count -------")
    for item in dict_transform(counter):
        if item["char"].isalpha() == True:
            print(f'{item["char"]}: {item["num"]}')
main()
