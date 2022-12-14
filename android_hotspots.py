from itertools import permutations
import string

letters = [str(i) for i in string.ascii_lowercase]
numbers = [str(i) for i in range(10)]

letter_perms = permutations(letters, 4)
number_perms = permutations(numbers, 4)

string_permutations = [''.join(permutation) for permutation in letter_perms]
number_permutations = [''.join(permutation) for permutation in number_perms]

f = open("hotspot_wordlist.txt", "w")
for i in string_permutations:
    for j in number_permutations:
        f.write(i + j)
f.close()
