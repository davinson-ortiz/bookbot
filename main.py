#! /usr/bin/python3

from stats import count_words, count_characters, sort_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: bookbot <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contens = get_book_text(file_path)
    num_words = count_words(file_contens)
    num_chars = count_characters(file_contens)
    sorted_characters = sort_characters(num_chars)
    print_report(file_path, num_words, sorted_characters)
    
    
def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
    
def print_report(file_path, num_words, sorted_characters):
    """Print a formatted report"""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_characters:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")
    
     
if __name__=="__main__":
    main()
