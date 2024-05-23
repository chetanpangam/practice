def print_rangoli(size):
    # your code goes here
    a_z = [chr(i) for i in range(97, 123)]
    
    rangoli = [("-".join(a_z[size-1 : i : -1] + a_z[i : size])).center((4*size)-3, "-") for i in range(size)]
    
    print("\n".join( rangoli[::-1] + rangoli[1:] ))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)