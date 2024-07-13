def separateNumbers(s):
    k = 1
    ans = False
    
    while k < len(s):
        n = int(s[:k])
        
        temp, i = str(n), 1
        while len(temp)<len(s):
            temp += str(n+i)
            i += 1
                
        if temp == s:
            ans = True
            break
        
        k += 1

    print(f"YES {n}" if ans else "NO")


separateNumbers("12345")
separateNumbers("91011")
separateNumbers("9991000")