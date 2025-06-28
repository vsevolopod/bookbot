#Bookbot v1.0 
############################
import sys
from stats import get_num_words
from stats import count_letters
from stats import sort_on
from stats import dict_list
try:
    file = sys.argv[1] 
except Exception:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(file)

    if text.isalpha():
        alpha = text
        print(alpha)
    
    words = get_num_words(text)
    letters = count_letters(text)
    listed = dict_list(letters)

    listed.sort(reverse = True, key = sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dicts in listed:
        get_alphas = dicts["char"]
        if get_alphas.isalpha() == True:
            print(f"{dicts["char"]}: {dicts["num"]}")
    print("============= END ===============")

main()