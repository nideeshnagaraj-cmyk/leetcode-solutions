def isPrefixOfWord(sentence, searchWord):
    s=sentence.split(' ')
    for i in s:
        if i.startswith(searchWord):
            Index=s.index(i)+1
            return Index
    else:
        return -1
print(isPrefixOfWord(sentence = "i am tired", searchWord = "you"))