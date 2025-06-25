def get_num_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    lowercase = text.lower()
    letters = []
    letter_counts = {}
    for char in lowercase:
        if char not in letters:
            letters.append(char)
   # print(f"letters", letters)
    for i in range (0, len(letters), 1):
        cur_letter = letters[i]
        count = 0
        #print(cur_letter)
        for letter in lowercase:
            if letter == cur_letter:
                count += 1
                letter_counts[cur_letter[0]] = count

    return letter_counts

        

