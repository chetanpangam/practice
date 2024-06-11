def allComb(s, current, index, result):
    result.append([''.join(current)])

    for i in range(index, len(s)):
        current.append(s[i])
        allComb(s,current, i+1, result)
        current.pop()


def findAllComb(s):
    current = []
    result = []
    index = 0
    
    allComb(s, current, index, result)
    print(result)       

findAllComb('scp')