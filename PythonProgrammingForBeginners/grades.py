#!/usr/bin/python3

def prompt():
  print ('Welcome to Grade Central')
  print ('')
  print ('[1] - Enter Grades')
  print ('[2] - Remove Student')
  print ('[3] - Student Average Grades')
  print ('[4] - Exit')
  choice = int(input('What would you like to do today? (Enter a number) '))
  
  return choice

def enterGrade(name,grade):
  print ('Adding Grade...')
  grades.append({name:grade})

def removeStudent(name):
  map(grades.pop, [name])

def averageGrade(name):
  list = []
  list = grades[name]
  

results=0
grades=[]

while results != 4:
  result=prompt()

  
  if result == 1:
    name  = input ('Student Name: ')
    grade = input ('Grade: ')
    enterGrade(name,grade)
    results=0
  
  if result == 2:
    name = input ('Student Name: ')
    removeStudent(name)
    results=0

  if result == 3:
    name  = input ('Student Name: ')
    averageGrade(name)
