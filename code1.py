#function to calculate gcd of two numbers.
def gcd(m,n):
    (x,y)=(max(m,n),min(m,n))
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)
        
print(gcd(24,16))
    