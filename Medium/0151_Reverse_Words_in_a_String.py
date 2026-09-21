def reverseWords(s):
    s=s.strip()
    s=s.split()
    rev=str('')
    for i in s:
        rev=i+' '+rev
    return rev.strip()
def reverseWords1(s):
    s=s.strip()
    s=s.split()
    return ' '.join(s[::-1])
print(reverseWords1("a good   example"))