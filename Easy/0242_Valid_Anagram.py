def isAnagram(s,t):
    if len(s)==len(t):
        s1=set(s)
        for i in s1:
            if s.count(i)!=t.count(i):
                return False
        else:
            return True
    else:
        return False
'''if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True'''
print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))