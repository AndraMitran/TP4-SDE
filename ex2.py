nr=int(input("N: "))

print("Prime numbers:",end=' ')

for n in range(1,nr):

    for i in range(2,n):

        if(n%i==0):

            break

    else:

        print(n,end=' ')    