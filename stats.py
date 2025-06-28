def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for lets in text:
        lcd = lets.lower()
        if lcd in letters:
            letters[lcd] +=1
        else:
            letters[lcd] = 1

    return letters

def dict_list(chars):
    char_dict = {}
    num_dict = {}
    full_dict = {}
    sort_list = []
    l_keys = list(chars.keys())
    l_vals = list(chars.values())
    for i in range (0, len(l_keys)):
        char_dict["char"] = l_keys[i] 
        num_dict["num"] = l_vals[i]
        full_dict = char_dict | num_dict
        sort_list.append(full_dict)

    return sort_list

def sort_on(items):
    return items["num"]


     
