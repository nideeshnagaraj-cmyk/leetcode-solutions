def findTheDifference(s, t):
        for i in t:
            if i in s:
                s=s.replace(i,'',1)
            else:
                return i
print(findTheDifference(s = "abcd", t = "abcde"))