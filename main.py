#! /usr/bin/python3

def main():
    book_path = "/home/davinson/PROGRAMMING/workspace/github.com/davinson-ortiz/bookbot/books/frankenstein.txt"
    text = read_book(book_path)
    number_of_words = count_words(text)
    char_counts = count_chars(text)
    sorted_char_counts = sort_char_counts(char_counts)
    print_report(book_path, number_of_words, sorted_char_counts)

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_char_counts(char_counts):
    return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

def print_report(book_path, num_words, sorted_char_counts):
    print(f"--- Begin report of {book_path.split("/")[-1]} ---")
    print(f"{num_words} words found in the document\n")
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()