#Bookbot v1.0 
############################
from stats import get_num_words
from stats import count_letters
from stats import sort_on
from stats import dict_list

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        #print("Contents inside:", file_contents)
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    
    if text.isalpha():
        alpha = text
        print(alpha)
    
    words = get_num_words(text)

    letters = count_letters(text)
    
    listed = dict_list(letters)



    listed.sort(reverse = True, key = sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath)
    print("----------- Word Count ----------")
    print(f"Found ",words, f"total words")
    print("--------- Character Count -------")
    for dicts in listed:
        get_alphas = dicts["char"]
        
        if get_alphas.isalpha() == True:
            print(dicts["char"], ":", dicts["num"])
    print("============= END ===============")

main()