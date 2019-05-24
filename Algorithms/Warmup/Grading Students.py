import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(len(grades)):
      if grades[i] < 38:
          print(grades[i])
      elif grades[i] >=38 and grades[i] <=40:
          print(40)
      elif grades[i]%10 <5 and ((grades[i]//10)*10 +5 -grades[i]) <3:
          print((grades[i]//10)*10 +5)
      elif grades[i]%10 >5 and ((grades[i]//10)*10 +10 -grades[i]) <3:
          print((grades[i]//10)*10 +5)
      else:
          print(grades[i])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
