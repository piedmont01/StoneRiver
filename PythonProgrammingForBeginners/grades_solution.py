#!/usr/bin/python3
from statistics import mean as m
admins = { 'Python':'Pass123@','user2':'pass2'}

studentDict = {'Jeff':[78,88,93], 'Alex':[92,76,88], 'Sam': [89,92,93] }

def enterGrades():
  name=input('Student Name: ')
  grade=input('Grade: ')

  if name in studentDict:
    print ('Adding Grade...')
    studentDict[name].append(float(grade))
  else:
    print('Student does not exist.')

  print(studentDict)

def removeStudent():
  nameToRemove = input('What student to remove: ')
  if nameToRemove in studentDict:
    print('removing student...')
    del studentDict[nameToRemove]
  else:
    print('Student does not exist.')

def averageGrade():
  for each in studentDict:
    gradeList = studentDict[each]
    avgGrade=m(gradeList)

    print(each,'has and average grade of ', avgGrade)
    

def main():
  print ('Welcome to Grade Central')
  print ('')
  print ('[1] - Enter Grades')
  print ('[2] - Remove Student')
  print ('[3] - Student Average Grades')
  print ('[4] - Exit')

  choice = int(input('What would you like to do today? (Enter a number) '))

  if choice == 1:
    enterGrades()
  elif choice == 2:
    removeStudent()
  elif choice == 3:
    averageGrade()
  elif choice == 4:
    exit()
  else:
    print('No valid choice was chosen.')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
  if admins[login] == passw:
    print('Welcome,',login)
    while True:
      main()
  else:
     print('Invalid password.')
else:
  print('Invalid username.')
  

