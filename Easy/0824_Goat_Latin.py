def toGoatLatin(sentence):#my coode
    words=sentence.split()
    latin=''
    j=1
    for i in words:
        if i[0] in 'aeiouAEIOU':
            latin=latin+' '+i+'ma'+'a'*j
        else:
            latin=latin+' '+i[1:]+i[0]+'ma'+'a'*j
        j+=1
    return latin[1:]
print(toGoatLatin("I speak Goat Latin"))

'''GPT code
def toGoatLatin(sentence):
    words = sentence.split()
    latin = []
    for j, word in enumerate(words, 1):
        if word[0] in 'aeiouAEIOU':
            new_word = word + 'ma' + 'a' * j
        else:
            new_word = word[1:] + word[0] + 'ma' + 'a' * j
        latin.append(new_word)
    return ' '.join(latin)
print(toGoatLatin("I speak Goat Latin"))'''