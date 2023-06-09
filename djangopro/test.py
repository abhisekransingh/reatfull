def m1(a,sqrtvalue):
    n=0
    for i in range(a):
        if(a!=0):
            a=a//sqrtvalue
            if(a!=0):
                n=n+1
        elif(a==0):
            break
    return n
        


r=m1(32,2)
print(r)
        

