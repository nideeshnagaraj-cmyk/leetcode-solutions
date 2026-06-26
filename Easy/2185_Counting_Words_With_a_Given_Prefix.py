def prefixCount(words, pref):
    Count=0
    for i in words:
        if i.startswith(pref):
            Count+=1
    return Count
print(prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))