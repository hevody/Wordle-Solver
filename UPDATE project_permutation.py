import copy

def permutations(inputs):
    perm = []
    listPoolCopy = copy.deepcopy(listPool)
    for letters in inputs:
        listLetters = list(letters)
        for letterRemove in listLetters:
            listPoolCopy.remove(letterRemove)
        for letra in listPoolCopy:
            newCon = letters + letra
            if newCon in perm:
                continue
            #print(newCon)
            perm = perm + [newCon]
        listPoolCopy = copy.deepcopy(listPool)
    return perm

print('What are the jumbled letters?')
pool = input()
listPool = list(pool)
print('How many digits?')
digits = int(input()) - 2

finalPerm = permutations(listPool)          # this is a list

for _ in range(digits):
    finalPerm += permutations(finalPerm)

with open('american-english') as f:
    english = f.readlines()

for word in english:
    word = word.lower()
    word = word.strip()
    if word in finalPerm:
        print(word)


