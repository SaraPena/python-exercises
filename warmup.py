import pandas as pd
import numpy as np

with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

print(words[:50])

# alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(alpha)
# alpha[0]

def word_math(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_letters = []
    for c in s:
        for l in alpha:
            if c == l:
                new_letters.append(l)
    "".join(new_letters)
    

word_math("AJKMZ")

"".join(['A', 'B', 'C'])

a = ['A', 'B', 'C']
k = ""
a[0].join(k)
k

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha.index("a".upper())


        