def length_of_last_word(s):
    s=s.strip(' ')
    word=0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            word+=1
        else:
            return word
    else:
            return word
print(length_of_last_word("a"))