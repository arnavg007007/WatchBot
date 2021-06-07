import time
import getpass
import threading
from Lib.DAO import StudentDAO as sDao
from Lib.VisionAPI import startRecoding

studentId = ''
stop_thread = False

def main():
    while True:
        global studentId
        studentId = input("Please Enter your Student's ID: ")
        password = getpass.getpass(prompt='Enter your password: ',stream=None)
        if(sDao.studentLogin(code=studentId, password=password) == True):
            print("Logged In")
            studentOperations()
            break
        do = input("\nLogin again (Y/N): ")
        if(do.lower() != 'y'):
            break

def studentOperations():
    while True:
        try:
            operationType = int(input("\n\n Lobby's Operations:\n1) Join the Class\n2) Check your dashboard\n3) Exit\n Select an operation: "))

            if (operationType == 1):
                classCode = input("Enter class code to start: ")
                joinClass(classCode)

            elif (operationType == 2):
                print("Checking DashBoard")
                
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


def joinClass(classCode):
    if (sDao.isClassStarted(classCode)) == False:
        return

    print("Entering the Class with code:'" + classCode + "'\n")
    
    global stop_thread

    ## First Thread to Save attentiveness on Firebase
    recordAttentivenessThread = threading.Thread(target=updateAttentiveData, args=(classCode,))
    recordAttentivenessThread.daemon = True

    ## Second Thread to continuosly get operation from class lobby. (If student leaves the class himself)
    classLobbyThread = threading.Thread(target=classLobby, args=(classCode,))
    classLobbyThread.daemon = True

    recordAttentivenessThread.start()
    classLobbyThread.start()
    while True:
        if stop_thread:
            print(">>>>>> Stopping Class" )
            recordAttentivenessThread.join()
            classLobbyThread.join()
            break
    

def classLobby(classCode):
    global stop_thread
    while True:
        if stop_thread:
            break
        try:
            operationType = int(input("\nClasses' Operations:\n1) Exit the Class\n2) Checking your attentiveness in this class\nSelect an operation: "))
            if (operationType == 1):
                try:
                    print("\nExiting..")
                    stop_thread = True
                except Exception as e:
                    print("Oops!", e.__class__, "occurred while Exiting.")
                finally:
                    break

            elif (operationType == 2):
                print('\nChecking dashboard.....')

            else:
                print("Please select a valid Operation number.")
                time.sleep(100)
        except ValueError as e:
            print("Please select a valid Operation number.")
        except Exception as e:
             print("Oops!", e.__class__, "occurred.")


def updateAttentiveData(classCode):
    attentiveness = 0
    global stop_thread
    while True:
        if(sDao.saveAttentiveness(sDao,attentiveness, studentId, classCode) != 'STOPPED'):
            attentiveness = startRecoding(1)
        else:
            stop_thread = True
        
        if stop_thread:
            break

    
if __name__ == '__main__':
    main()
