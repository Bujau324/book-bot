import sys
from stats import word_count, character_count, sorted_list_of_dicts



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = "./" + sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(book_path))} total words")
    print("--------- Character Count -------")
    sorted = sorted_list_of_dicts(character_count(get_book_text(book_path)))
    for dictionary in sorted:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()
