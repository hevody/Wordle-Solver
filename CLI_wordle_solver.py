import wordle_solver_main
import json

### opens cli json ###
with open('./resources/cli.json') as f:
    cli_display = json.load(fp=f)
### --- ###

modes = {'wordle solver': wordle_solver_main.wordle_solver, 
         'jumbled letters solver (best for wordscapes, 4pics1word, anagrams)': wordle_solver_main.jumbled_letters_solver}  # this is a little bit slow
modes_list = list(modes.keys())

print(cli_display["MODE_MENU"])

for mode in modes:
    print(f'[{modes_list.index(mode) + 1}] {mode}')

chosen_mode = int(input('\n> ')) - 1

if modes[modes_list[chosen_mode]] == wordle_solver_main.wordle_solver:
    print(f'{list(cli_display["EXAMPLE"].keys())[0]}')
    for index in range(len(list(cli_display["EXAMPLE"]["\nExample:"].keys()))):
        example_key = list(cli_display["EXAMPLE"]["\nExample:"].keys())[index]
        example_value = cli_display["EXAMPLE"]["\nExample:"][example_key]
        print(f'    {example_key.ljust(14)}: {example_value}')

    known_letters = input('known letters'.ljust(14) + ': ')       # use regex so finding the words in the dictionary will be easy
    bad_letters = input('bad letters'.ljust(14) + ': ')
    clue_letters = input('clue letters'.ljust(14) + ': ')                

    results = modes[modes_list[chosen_mode]](known_letters=known_letters, bad_letters=bad_letters, clue_letters=clue_letters)

    print(cli_display["hpw"])
    for word in results[0]:
        print(f'[*] {word}')

    print(cli_display["bcl"])
    for word in results[1]:
        print(f'[*] {word}')

if  modes[modes_list[chosen_mode]] == wordle_solver_main.jumbled_letters_solver:
    print(cli_display["JUMBLED_question1"])
    pool = input('\n> ')
    print(cli_display["JUMBLED_question2"])
    length = int(input())
    print(cli_display["JUMBLED_running1"])
    result = wordle_solver_main.jumbled_letters_solver(pool=pool, length=length)
    print(cli_display["JUMBLED_running2"])
    for word in result[0]:
        print(f'[*] {word}')
    print(cli_display["JUMBLED_running3"])
    for word in result[1]:
        print(f'[*] {word}')
    