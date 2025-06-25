#Bookbot v1.0 
############################
from stats import get_num_words
from stats import count_letters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        #print("Contents inside:", file_contents)
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print (get_num_words(text), f"words found in the document")
    letters = count_letters(text)
    print (f"count" , letters)

main()