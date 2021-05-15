def fact(N):
    
    if N==0:
        return 1
    else:
        return N*fact(N-1)

for i in range(21):
    print('{0}!={1}'.format(i,fact(i)))

