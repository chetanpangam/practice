# PrimeNumber.py

def isPrime(num):
    mid = num//2

    if num == 0 or num == 1:
        return False

    for i in range(2,mid + 1):
        if num % i == 0:
            return False
    
    return True


# num = 17
# num = 23
num = 2
# num = 16

print(f'Is number {num} a prime number? - {isPrime(num)}')