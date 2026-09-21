def defangIPaddr(address):
    res=''
    for i in address:
        if i=='.':
            res+='[.]'
        else:
            res+=i
    return res
print(defangIPaddr(address = "255.100.50.0"))
'''
res=address.replace('.','[.]')
return res
'''