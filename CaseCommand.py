# CaseCommand.py
'''
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  
types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
def perform_operations(arr, op_command, e, i):
    match op_command: #works with python 3.10 and above
        case "insert":
            arr.insert(i,e)
        case "print":
            print(arr)
        case "remove":
            arr.remove(e)
        case "append":
            arr.append(e)
        case "sort":
            arr.sort()
        case "pop":
            arr.pop()
        case "reverse":
            arr.reverse()

def parseargs(args):
    if len(args) == 2:
        i = args[0]
        e = args[1]
        return int(e), int(i)
    else:
        e = args[0]
        return int(e), None
    
    

if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        op_command , *args = input().split(" ")

        if args:
            e, i = parseargs(args)

        perform_operations(arr, op_command, e, i)