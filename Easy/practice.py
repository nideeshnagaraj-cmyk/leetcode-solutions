j=0
n=15
print(1)

for i in range(2,n+1):
    if n%i==0:
        if j==0:
            print("Fizz")
            j+=1
        else:
            print("Buzz")
            j=0
    else:
        print(i)