def findWordsContaining(words, x):
    y=[i for i in range(len(words)) if x in words[i]]
    return y
print(findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a"))