from itertools import permutations
s=input("Enter the sentence: ").split()
words=permutations(s,len(s))
for i in words:
    sen=' '.join(i)
    print(sen)
