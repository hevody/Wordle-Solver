import copy



pool = 'usemoxwiuocz'

listPool = list(pool)
listPoolCopy = copy.deepcopy(listPool)

perm2 = []
for letter in listPool:
    listPoolCopy.remove(letter)
    for concat in listPoolCopy:
        perm2 = perm2 + [letter + concat]
    listPoolCopy = copy.deepcopy(listPool)

print(perm2)

perm3 = []

listPoolCopy = copy.deepcopy(listPool)

for letters in perm2:
    listLetters = list(letters)
    for letterRemove in listLetters:
        listPoolCopy.remove(letterRemove)
    for letra in listPoolCopy:
        print(letters + letra)
        perm3 = perm3 + [letters + letra]
    listPoolCopy = copy.deepcopy(listPool)

perm4 = []
for letters in perm3:
    listLetters = list(letters)
    for letterRemove in listLetters:
        listPoolCopy.remove(letterRemove)
    for letra in listPoolCopy:
        print(letters + letra)
        perm4 = perm4 + [letters + letra]
    listPoolCopy = copy.deepcopy(listPool)
    
perm5 = []
for letters in perm4:
    listLetters = list(letters)
    for letterRemove in listLetters:
        listPoolCopy.remove(letterRemove)
    for letra in listPoolCopy:
        print(letters + letra)
        perm5 = perm5 + [letters + letra]
    listPoolCopy = copy.deepcopy(listPool)

'''
perm6 = []
for letters in perm5:
    listLetters = list(letters)
    for letterRemove in listLetters:
        listPoolCopy.remove(letterRemove)
    for letra in listPoolCopy:
        print(letters + letra)
        perm6 = perm6 + [letters + letra]
    listPoolCopy = copy.deepcopy(listPool)
'''

print(len(perm5))

if 'mouse' in perm5:
    print('MOUSE FOUND!')

#print(perm3)
