def add2numbers(x,y):
    return x+y

def sub2numbers(x,y):
    return x-y

def mul2numbers(x,y):
    return x*y

def div2numbers(x,y):
    return x/y

if __name__ =="__main__":
    a=int(input("Enter the 1st number"))
    b=int(input("Enter the 2nd number"))
    sum=add2numbers(a,b)
    diff=sub2numbers(a,b)
    prod=mul2numbers(a,b)
    div=div2numbers(a,b)
    print(sum)
    print(diff)
    print(prod)
    print(div)
