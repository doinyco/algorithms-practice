# Find the greatest common denominator of two numbers using Euclid's algorithm 

def gcd(a, b):

    while b!= 0:
        temp = a
        a = b
        b = temp % b

    return a 

print(gcd(60, 96))
print(gcd(20, 8))
