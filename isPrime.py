

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
    
for n in range(1000000):
    r = n * n + n + 41
    if(not test_prime(r)):
        print(r)
        exit()
