def canConstruct(ransomNote,magazine):
    count=0
    s=set(magazine)
    for i in s:
        if i in ransomNote:
            if magazine.count(i)>=ransomNote.count(i):
                count+=ransomNote.count(i)
    return count==len(ransomNote)
'''if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True'''
print(canConstruct(ransomNote = "aab", magazine = "baa"))