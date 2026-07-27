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
            print(newCon)
            perm = perm + [newCon]
        listPoolCopy = copy.deepcopy(listPool)
    return perm

print('What are the jumbled letters?')
pool = input()
listPool = list(pool)
print('How many digits?')
digits = input()
digits = int(digits)

twoPerm = permutations(listPool)
threePerm = permutations(twoPerm)
#thirdPerm = permutations(secondPerm)
#fourthPerm = permutations(thirdPerm)
#fifthPerm = permutations(fourthPerm)

#dprint(fourthPerm)

finalPerm = []


if digits == 2:
    finalPerm = permutations(listPool)

if digits == 3:
    twoPerm = permutations(listPool)
    finalPerm = permutations(twoPerm)

if digits == 4:
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    finalPerm = permutations(threePerm)

if digits == 5:
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    fourPerm = permutations(threePerm)
    finalPerm = permutations(fourPerm)

if digits == 6:
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    fourPerm = permutations(threePerm)
    fivePerm = permutations(fourPerm)
    finalPerm = permutations(fivePerm)

if digits == 7:
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    fourPerm = permutations(threePerm)
    fivePerm = permutations(fourPerm)
    sixPerm = permutations(fivePerm)
    finalPerm = permutations(sixPerm)

if digits == 8:
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    fourPerm = permutations(threePerm)
    fivePerm = permutations(fourPerm)
    sixPerm = permutations(fivePerm)
    sevenPerm = permutations(sixPerm)
    finalPerm = permutations(sevenPerm)

if digits == 9: 
    twoPerm = permutations(listPool)
    threePerm = permutations(twoPerm)
    fourPerm = permutations(threePerm)
    fivePerm = permutations(fourPerm)
    sixPerm = permutations(fivePerm)
    sevenPerm = permutations(sixPerm)
    eightPerm = permutations(sevenPerm)
    finalPerm = permutations(eightPerm)


print(finalPerm)

with open('american-english') as f:
    english = f.readlines()

#words = []
for word in english:
    word = word.lower()
    word = word.strip()
    if word in finalPerm:
        print(word)


