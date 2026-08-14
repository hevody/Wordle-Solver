import copy

def permutations(potential_words_array: list) -> list:                        # side-note: although I use the terms word and letters, this can also apply to numbers
    ### variable declaration ###
    permutated_list = []
    listPoolCopy = copy.deepcopy(listPool)                                    # we copy so we can add letters into it
    ### --- ###
    for potential_word in potential_words_array:
        listLetters = list(potential_word)
        for letterRemove in listLetters:
            listPoolCopy.remove(letterRemove)                                 # removes a given letter if found present in the previous potential word, the only remaining ones are concatenated in the new potential word
        for remaining_letter in listPoolCopy:
            new_potential_word = potential_word + remaining_letter            # contains the permutated string
            if new_potential_word in permutated_list:
                continue
            permutated_list += [new_potential_word]                           # adds the new potential word to the permutated list
        listPoolCopy = copy.deepcopy(listPool)
    return permutated_list

if __name__ == '__main__':
    # Future feature: ??ilo
    print('\nWhat are the jumbled letters?')
    print('Example: degeo')
    pool = input('\n> ')
    listPool = list(pool)
    print('\nWhat is the length of the word?')
    length = int(input()) - 2                   # we subtracted 2 because of the line `finalPerm = permutations(listPool)`

    finalPerm = permutations(listPool)          # this is a list

    for _ in range(length):
        finalPerm += permutations(finalPerm)

    with open('american-english') as f:
        english = f.readlines()

    word_w_exact_length = []
    print('\n[RUNNING] dictionary check...')
    for word_verbatim in english:
        word_verbatim = word_verbatim.strip()
        word = word_verbatim.lower()
        word = word.strip()
        if word in finalPerm:
            print(f'[*] {word_verbatim}')
            if len(word) == length + 2:
                word_w_exact_length += [word_verbatim]

    print('\n[RUNNING] found word with exact length...')
    for exact_word_candidate in word_w_exact_length:
        print(f'[*] {exact_word_candidate}')


