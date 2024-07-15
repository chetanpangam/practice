def factorial(n):
    import pdb
    pdb.set_trace()
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

factorial(5)