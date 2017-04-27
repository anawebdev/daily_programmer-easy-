
'''
number 1-1000
1.The number has two or more digits. X
2.The number is prime. X
3.The number does NOT contain a 1 or 7 in it. 
4.The sum of all of the digits is less than or equal to 10. X
5.The first two digits add up to be odd.X
6.The second to last digit is even.x
7.The last digit is equal to how many digits are in the number.

'''

def cond_2(x):
    n=int(x/2+1)
    for i in range(2,n):
        if x%i==0:
            return False
    return True
def cond_3(x):
    n=x
    for i in range(1,4):
        if n%10==1 or n%10==7:
            return False
        else:
            n=n//10
    return True    
def cond_4(x):
    n=list(str(x))
    total=0
    for i in range(len(n)):
        total = total + int(n[i])
    if total > 10:
        return False
    else:
        return True
def cond_5(x):
    if x in range(10, 100):
        nr=(x//10)+(x%10)
        if nr%2 == 0:
            return False
        return True
    if x in range (100,1000):
        n=x//10
        nr=(n//10)+(n%10)
        if nr%2==0:
            return False
        return True

def cond_6(x):
    '''second to last is even'''
    n=x//10
    n=n%10
    if n % 2 == 0:
        return True
    else:
        return False
def cond_7(x):
    '''last digit = number of digits in the number'''
    if x in range(10,100):
        num=2
    elif x in range(100,1000):
        num=3
    if x%10==num:
        return True
    return False
def whatsmynumber():
    
    for x in range(10,1000):
        if cond_2(x):
            if cond_3(x):
                if cond_4(x):
                    if cond_5(x):
                        if cond_6(x):
                            if cond_7(x):
                                print (x)
whatsmynumber()
