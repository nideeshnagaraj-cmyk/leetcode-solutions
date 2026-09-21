def mergeAlternately(word1,word2):
    if len(word1)>len(word2):
        word2=word2+' '*(len(word1)-len(word2))
    elif len(word2)>len(word1):
        word1=word1+' '*(len(word2)-len(word1))
    result=''
    for i in range(len(word1)):
        result=result+word1[i]+word2[i]
        result=result.replace(' ','')
    print(result)
mergeAlternately(word1="abcd",word2="pq")