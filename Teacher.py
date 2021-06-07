import time
import getpass
from Lib.DAO import TeacherDAO as tDao

teacherId = ''

def main():
    while True:
        global teacherId
        teacherId = input("Please Enter your Teacher's ID: ")
        password = getpass.getpass("Enter your password: ")
        if(tDao.teacherLogin(code=teacherId, password=password) == True):
            print("Logged In")
            teacherOperations()
            break
        do = input("\nLogin again (Y/N): ")
        if(do != 'y' and do != 'Y'):
            break

def teacherOperations():
    while True:
        try:
            operationType = int(input("\n\nOperations:\n1) Create Class\n2) Start a Class\n3) Exit\n Select an operation: "))

            if (operationType == 1):
                createClass()

            elif (operationType == 2):
                classCode = input("Enter class code to start: ")
                startClass(classCode)
            elif (operationType == 3):
                print("See you soon.......")
                time.sleep(2)
                exit()
            else:
                print("Please select a valid Operation number.")
        except ValueError as e:
            print("Please select a valid Operation number.")
        except Exception as e:
             print("Oops!", e.__class__, "occurred.")
        

def createClass():
    classCode = tDao.createNewClass(tDao, teacherId)
    print('Class Created: ' + classCode)

def startClass(classCode):
    if (tDao.startClass(classCode)) == False:
        return

    print("Entering the Class with code:'", classCode, "'\n")
    while True:
        try:
            operationType = int(input("\n\nOperations:\n1) Stop the Class\n2) Check dashboard\n3) Go back to app lobby\nSelect an operation: "))

            if (operationType == 1):
                tDao.stopClass(classCode)

            elif (operationType == 2):
                print('Checking dashboard.....')

            elif (operationType == 3):
                print()
                break
        except ValueError as e:
            print("Please select a valid Operation number.")
        except Exception as e:
             print("Oops!", e.__class__, "occurred.")
    
if __name__ == '__main__':
    main()
