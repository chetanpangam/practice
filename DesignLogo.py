# DesignLogo.py
"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. 
Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
"""


#Function to sort multiple attribute
def multisort(items, specs):
    for i , reverse in reversed(specs):
        items.sort(key=lambda x: x[i], reverse=reverse)
    return items

if __name__ == '__main__':
    s = input()
    # s="ccbbbaade"

mydict = {}
for ch in s:
    mydict[ch] = mydict.get(ch, 0) + 1

items = list(mydict.items())
new_dict = dict(multisort(items, [(1, True), (0, False)]))

print("========= First Way=========")
counter = 0
for key, val in new_dict.items():
    if counter > 2:
        break
    print(key + " " + str(val))
    counter += 1


print("========= Second Way=========")
second_result = dict(sorted(mydict.items(), key=lambda x: (-x[1],x[0])))


counter1 = 0
for key, val in second_result.items():
    if counter1 > 2:
        break
    print(key + " " + str(val))
    counter1 += 1