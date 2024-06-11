import operator

def person_lister(f):
    print("In person_lister")
    def inner(people):
        print("In inner")
        result = sorted(people, key=lambda x: int(x[2]))
        # return (("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1] for person in result)
        return map(f, result)
    return inner

@person_lister
def name_format(person):
    print("In name_format")
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    print("In Main")
    # people = [input().split() for i in range(int(input()))]
    people = [['Jake', 'Jake', '42', 'M'], ['Jake', 'Kevin', '57', 'M'], ['Jake', 'Michael', '91', 'M'], \
              ['Kevin', 'Jake', '2', 'M'], ['Kevin', 'Kevin', '44', 'M'], ['Kevin', 'Michael', '100', 'M'], \
              ['Michael', 'Jake', '4', 'M'], ['Michael', 'Kevin', '36', 'M'], ['Michael', 'Michael', '15', 'M'], \
              ['Micheal', 'Micheal', '6', 'M']]
    print(*name_format(people), sep='\n')


'''
Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''