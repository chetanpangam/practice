'''
Given an array of N integers, write a function to return the maximum numbers from the array such that all the numbers have same difference between each of them:
E.g.:- arr = [12,12,12,15,13,14]
o/p:- 4 (12,13,14,15)
'''

def maxNumInArray(arr):
    count = 0
    listt = list(set(arr))
    mapp = {}
    print(listt)
    for i in range(len(listt)-1):
        for j in range(i+1, len(listt)):
            diff = abs(listt[j] - listt[i])
            mapp[diff] = mapp.get(diff, 0) + 1
    result = sorted(mapp.items(), key=lambda x: (-x[1]))

    print(result)
    return result[0][1] + 1

# arr =  [12,12,12,15,13,14]
arr = [20,1,15,3,10,5,8]
print(maxNumInArray(arr))