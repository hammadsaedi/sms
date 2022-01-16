import os
import time

def main():
  # Clear Screen
  clearConsole()
  # Header
  print(format("STUDENT MANAGEMENT SYSTEM\n", ">30s"))
  # Main Menu
  print("MAIN MENU:")
  print("1: Showing the List of Student")
  print("2: Add New Student Data")
  print("3: Search Student Data")
  print("4: Delete any Student Data")
  print("0: Exit Program")
  # taking choice
  choice = int(input("\nSelect Any Option (0 - 4): "))
  # Conditional Statement to take action depending upon user input
  if choice == 1:
    displayStudent()
  elif choice == 2:
    addStudent()
  elif choice == 3:
    searchStudent()
  elif choice == 4:
    deleteStudent()
  elif choice == 0:
    # Clear Screen
    clearConsole()
    print("Closing Program")
    time.sleep(2)
    # Clear Screen
    clearConsole()
    exit()
  else:
      print("Error: Please input numbers from 0 to 4 as a choice")
      time.sleep(1)
      main()


# Clear Console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# to display Studnet List
def displayStudent():
  # Clear Screen
  clearConsole()
  # Serial Number
  i = 1
  # Looping through List
  for student in studentList:
    print(f'{i}: {student}')
    # Incrementin Serial Number
    i += 1
  # Spacing
  print()
  # to continue
  toContinueStudentList()


# to continue Student List 
def toContinueStudentList(): 
  # Menu
  print("Choose any option:")
  print("1: Main Menu")
  print("0: Exit Program")
   # taking choice
  choice = int(input("\nSelect Any Option (0 - 1): "))
  # Conditional Statement to take action depending upon user input
  if choice == 1:
    main()
  elif choice == 0:
    # Clear Screen
    clearConsole()
    print("Closing Program")
    time.sleep(2)
    # Clear Screen
    clearConsole()
    exit()
  else:
    print("Error: Please input numbers from 0 to 1 as a choice")
    time.sleep(1)
    toContinueStudentList()


# to add Student
def addStudent():
  # Clear Screen
  clearConsole()
  # New Student
  newStudent = input("Enter Student Name: ")
  if(newStudent in studentList):
    print(f"{newStudent} is already in the table")
  else:
    print(f'New Student {newStudent} is added, successfully.\n')
  # to Continue
  toContinueAddStudent()


# to Continue Add Student
def toContinueAddStudent():
  # Menu
  print("Choose any option:")
  print("1: Add another Student")
  print("2: Main Menu")
  print("0: Exit Program")
   # taking choice
  choice = int(input("\nSelect Any Option (0 - 2): "))
  # Conditional Statement to take action depending upon user input
  if choice == 1:
    addStudent()
  elif choice == 2:
    main()
  elif choice == 0:
    # Clear Screen
    clearConsole()
    print("Closing Program")
    time.sleep(2)
    # Clear Screen
    clearConsole()
    exit()
  else:
    print("Error: Please input numbers from 0 to 2 as a choice")
    time.sleep(1)
    toContinueAddStudent()
    

# to search Student
def searchStudent():
  # Clear Screen
  clearConsole()
  # Taking input
  desiredStudent = input("Enter Student Name To Search: ")
  # Conditional Statement to take action depending upon user input
  if(desiredStudent in studentList):
    print(f"{desiredStudent} is present in Data set.\n")
    toContinueSearchStudent()
  else:
    print(f"{desiredStudent} is not present in Data set.\n")
    toContinueSearchStudent()



# to continue search Student
def toContinueSearchStudent():
  # Menu
  print("Choose any option:")
  print("1: Search Another Student")
  print("2: Main Menu")
  print("0: Exit Program")
   # taking choice
  choice = int(input("\nSelect Any Option (0 - 2): "))
  # Conditional Statement to take action depending upon user input
  if choice == 1:
    searchStudent()
  elif choice == 2:
    main()
  elif choice == 0:
    # Clear Screen
    clearConsole()
    print("Closing Program")
    time.sleep(2)
    # Clear Screen
    clearConsole()
    exit()
  else:
    print("Error: Please input numbers from 0 to 2 as a choice")
    time.sleep(1)
    toContinueSearchStudent()


# to delete Student
def deleteStudent():
  # Clear Screen
  clearConsole()
  # Taking Input
  desiredStudent = input("Enter Student Name to Delete: ")
	# Conditional Statement to take action depending upon user input'
  if desiredStudent in studentList:
    studentList.remove(desiredStudent)
    print(f'{desiredStudent} is successfully, deleted.\n')
    toContinueDeleteStudent()
  else:
    print(f'There is no {desiredStudent} present in data set.\n')
    toContinueDeleteStudent()


# to continue search Student
def toContinueDeleteStudent():
  # Menu
  print("Choose any option:")
  print("1: Delete Another Student")
  print("2: Main Menu")
  print("0: Exit Program")
   # taking choice
  choice = int(input("\nSelect Any Option (0 - 2): "))
  # Conditional Statement to take action depending upon user input
  if choice == 1:
    deleteStudent()
  elif choice == 2:
    main()
  elif choice == 0:
    # Clear Screen
    clearConsole()
    print("Closing Program")
    time.sleep(2)
    # Clear Screen
    clearConsole()
    exit()
  else:
    print("Error: Please input numbers from 0 to 2 as a choice")
    time.sleep(1)
    toContinueSearchStudent()


# Student List
studentList = ["Hammad", "Fareh", "Ahtasham"]


# Callling Main Function
main()
