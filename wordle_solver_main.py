import copy
import re
import json

### config ###
with open('config.json') as f:
    config = json.load(fp=f)

dictionary = config['dictionary']
### --- ###

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

def JUMBLE_search_in_dictionary(permutation_list: list, to_exact_length: int):
    with open(dictionary) as f:
        english = f.readlines()

    word_w_exact_length = []
    print('[RUNNING] dictionary check...')
    for word_verbatim in english:
        word_verbatim = word_verbatim.strip()
        word = word_verbatim.lower()
        word = word.strip()
        if word in permutation_list:
            print(f'[*] {word_verbatim}')
            if len(word) == to_exact_length + 2:
                word_w_exact_length += [word_verbatim]

    print('\n[RUNNING] found words with exact length...')
    for exact_word_candidate in word_w_exact_length:
        print(f'[*] {exact_word_candidate}')

def jumbled_letters_solver():
    global listPool

    print('\nWhat are the jumbled letters?')
    print('Example: degeo')
    pool = input('\n> ')
    listPool = list(pool)
    print('\nWhat is the length of the word?')
    length = int(input()) - 2                   # we subtracted 2 because of the line `finalPerm = permutations(listPool)`

    print('\n[RUNNING] permutations')
    finalPerm = permutations(listPool)          # this is a list

    for _ in range(length):
        finalPerm += permutations(finalPerm)

    JUMBLE_search_in_dictionary(finalPerm, to_exact_length=length)

def generate_a_regex_pattern(the_known_letters: list):
    generated_pattern = r''
    for letter in the_known_letters:
        if letter == '?':
            letter = '.'
        generated_pattern += letter
    return fr'^{generated_pattern}$'

def wordle_solver():
    print('''\nExample:
    known letters: ?e??e        
    bad letters: cranmiht
    clue letters: og
    ''')

    known_letters = list(input('known letters: '))       # use regex so finding the words in the dictionary will be easy
    bad_letters = list(input('bad letters: '))
    clue_letters = list(input('clue letters: '))                # this will be permutated, change of plans, no 

    pattern = re.compile(fr'{generate_a_regex_pattern(known_letters)}')

    matched_words = []
    with open(dictionary) as f:
        for line in f: 
            word = line.strip()
            word = word.lower()
            if pattern.search(word):
                matched_words += [word]

    
    list_contains_bad_letters = []
    for letter in bad_letters:
        for word in matched_words:
            if letter in word:
                list_contains_bad_letters += [word]
            else:
                continue

    for word in list_contains_bad_letters:
        try:
            matched_words.remove(word)
        except:
            continue

    possible_words = []
    for word in matched_words:
        word_array = list(word)
        if all(item in word_array for item in clue_letters):
            possible_words += [word]

    with open(dictionary) as f:
        the_dictionary = f.readlines()

    print('[RUNNING] high potential words...')
    for based_word in the_dictionary:
        based_word = based_word.strip()
        based_word_lower = based_word.lower()
        for word in possible_words:
            if based_word_lower == word:
                print(f'[*] {based_word}')

    dictionary_words = []
    for line in the_dictionary:
        dictionary_words += [line.strip()]

    filtered_matched_words = []
    print('\n[RUNNING] finding possible words based on the clue letters...')
    for possible_word in possible_words:
        for word in dictionary_words:
            lower_case_dictionary_word = word.lower()
            if lower_case_dictionary_word == possible_word:
                filtered_matched_words += [word]

    for word in filtered_matched_words:
        word_array = word.lower()
        word_array = list(word_array)
        if all(item in clue_letters for item in word_array):
            print(f'[*] {word}')

if __name__ == '__main__':
    modes = {'wordle solver': wordle_solver, 
             'jumbled letters solver (best for anagrams, wordscapes, 4pics1word)': jumbled_letters_solver}  # this is a little bit slow
    modes_list = list(modes.keys())

    print('\nWhich MODE would you like to choose?')   
    for mode in modes:
        print(f'[{modes_list.index(mode) + 1}] {mode}')

    chosen_mode = int(input('\n> ')) - 1
    modes[modes_list[chosen_mode]]()