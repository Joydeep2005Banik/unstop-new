A,B=map(int,input().split())

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

lcm=abs(A*B) // gcd(A,B)
print(lcm)