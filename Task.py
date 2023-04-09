# Date 13 Mar 2023
# Author Volodymyr Yaremenko
# Task - 3 files Exercise Menu
import os
import getpass

names=[]
hours=[]
rate=[]
wages=[]

def read_names():
  testFile=open("names.txt","r")
  for line in testFile:
    stripped=line.strip()
    names.append(stripped)
  testFile.close()

def read_hours():
  testFile=open("hours.txt","r")
  for line in testFile:
    stripped=line.strip()
    hours.append(stripped)
  testFile.close()

def read_rate():
  testFile=open("rate.txt","r")
  for line in testFile:
    stripped=line.strip()
    rate.append(stripped)
  testFile.close()

def calc_wages():
  for x in range(len(names)):
    wages.append(float(rate[x]) * float(hours[x]))

def print_wages():
  for x in range(len(names)):
   print("\n", names[x], " wages are £ ",round(wages[x],2))

def get_min():
  min = wages[0]
  for x in range(len(names)):
    if (min > wages[x]):
      min = wages[x]
  print (" Min wage is £ ",min)

def get_max():
  max = wages[0]
  for x in range(len(names)):
    if (max < wages[x]):
      max = wages[x]
  print (" Max wage is £ ",max)  

def wage100():
  count=0
  for x in range (len(wages)):
    if (wages[x]<100):
      count=count+1
  print("Number of wages below £100 is ", count)
      
def menu():
  print ("Welcome to the Menu!")
  print()
  print("1 : Read from file")
  print("2 : Calc wages")
  print("3 : Display wages")
  print("4 : Get max")
  print("5 : Get min")
  print("6 : Wages under 100")
  print("7 : Exit")
  print()

for x in range(3):
  login = input("Please enter login : ")
  pwd = getpass.getpass()
  if (login=="") and (pwd == ""):
    print()
    choice =0
    while ( choice!=7 ):
      input("Press enter key to continue ")
      os.system("clear")
      menu()
      choice=int(input("Choose a menu option : "))
      if ( choice==1):
        read_hours()
        read_rate()
        read_names()
      elif ( choice==2):
        calc_wages()
      elif ( choice==3):
        print_wages()
      elif ( choice ==4):
        get_max()
      elif (choice==5):
        get_min()
      elif (choice==6):
        wage100()
      elif (choice==7):
        print("Goodbye")
      else:
        print("Incorrect choice !")
    break
  else:
    print ("Incorrect login attempt ", x+1)
