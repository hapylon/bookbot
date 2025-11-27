# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
        
#     return file_contents
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

from stats import word_count
from stats import char_counts
from stats import char_dicts

def main():
    dict = char_counts(filepath)
    list = char_dicts(filepath)
    intro1 = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------"""
    intro2 = "--------- Character Count -------"
    print(intro1)
    word_count(filepath)
    print(intro2)
    for i in list:
        print(f"{i["char"]}: {i["num"]}")
    
main()