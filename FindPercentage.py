# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

import math

def calPercentage(score_list):
    avg = float(sum(score_list)/len(score_list))
    return format(avg, '.2f')
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        temp_list = student_marks.get(query_name)
    
    print(calPercentage(temp_list))
