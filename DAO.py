import pyrebase
import datetime
from Lib.FirebaseConnection import getFirebaseDb

class TeacherDAO:
    def teacherLogin(code, password):
        check = False
        db = getFirebaseDb()
        user = db.child("USER").child(code).get()
        user = user.val()
        if user is not None:
            if user.get("TYPE") != "TEACHER":
                print("Not a Teacher. Please login from Student portal.")
            elif user.get("PASSWORD") != password:
                print("Invalid password.")
            else:
                check = True
                
        else:
            print("User Id may be wrong.")

        return check

    def createNewClass(self,teacherCode):
        db = getFirebaseDb()
        seq = db.child("CLASS_SEQ").get()
        seq = seq.val()
        #print('creating')
        '''Updating new sequence'''
        db.update({"CLASS_SEQ": seq+1})

        #print('Getting new Class Obj')
        newClass = self.getClassJson(teacherCode,seq)
        print('new class', newClass)
        classCode = "CLASS"+str(seq)
        db.child("CLASS").child(classCode).set(newClass)
        
        return classCode

    def startClass(classCode):
        db = getFirebaseDb()
        isStarted = False
        
        #Getting class from DB
        classObject = db.child("CLASS").child(classCode).get()
        classObject = classObject.val()

        if classObject is not None:
            status = classObject.get("STATUS")
            if(status == "STARTED"):
                print("Class is already " + status)
                isJoin = input("Would you like to join? (Y/N)")
                if(isJoin == 'Y' or isJoin == 'y'):
                    isStarted = True

            elif(status == "STOPPED"):
                print("Cannot Start, Class is already " + status + ".")
            else:
                status = "STARTED"
                classObject["STATUS"] = status
                db.child("CLASS").child(classCode).set(classObject)
                isStarted = True
                
        else: 
            print("No Such CLASS found.")

        return isStarted

    def stopClass(classCode):
        db = getFirebaseDb()
        
        #Getting class from DB
        classObject = db.child("CLASS").child(classCode).get()
        classObject = classObject.val()

        if classObject is not None:
            status = classObject.get("STATUS")
            if(status == "STOPPED"):
                print("Class is already " + status)
                print("Please choose different operation")
            else:
                classObject["STATUS"] = "STOPPED"
                db.child("CLASS").child(classCode).set(classObject)
                print("'"+ classCode + "' Stopped.")
                            
        else: 
            print("No Such CLASS found.")
        
    def getClassJson(teacherCode, seq):
        today = datetime.datetime.now()

        classObj = {
          "CODE": "CLASS"+str(seq),
          "TEACHER": teacherCode,
          "DATE": str(today),
          "STATUS":"NEW"
        }
        
        return classObj

class StudentDAO:
    
    def studentLogin(code, password):
        check = False
        db = getFirebaseDb()
        user = db.child("USER").child(code).get()
        user = user.val()
        if user is not None:
            if user.get("TYPE") != "STUDENT":
                print("Not a Teacher. Please login from Student's ID.")
            elif user.get("PASSWORD") != password:
                print("Invalid password.")
            else:
                check = True
                
        else:
            print("User Id may be wrong.")

        return check

    def isClassStarted(classCode):
        isStarted = False
        db = getFirebaseDb()
        cls = db.child("CLASS").child(classCode).get()
        cls = cls.val()
        status = cls.get('STATUS')
        if status == 'NEW':
            print('Class not started yet. Join again later.')
        elif status == 'STOPPED':
            print('Class already ended.')
        elif status == 'STARTED':
            print('Joining....')
            isStarted = True
        else:
            print("Some error occured. Please Teacher to start the class again.")

        return isStarted
    
    def saveAttentiveness(self,attentiveness, user, classCode):
        db = getFirebaseDb()
        print('>>> Uploading confidence:', attentiveness)
        classRecord = db.child("CLASS").child(classCode).get().val()
        if classRecord.get('STATUS') == 'STOPPED':
            return 'STOPPED'
        classUserRecord = db.child("CLASS_ATTENTIVENESS").child(classCode + '_' + user).get()
        classUserRecord = classUserRecord.val()

        if classUserRecord is None:
            classUserRecord = self.getClassUserJson(classCode, user, attentiveness, db)
        else:
            classUserRecord['ATTENTIVENESS'] = attentiveness
        
        db.child("CLASS_ATTENTIVENESS").child(classCode + '_' + user).set(classUserRecord)

    
    def getClassUserJson(classCode, user, attentiveness,db):
        today = datetime.datetime.now()

        userRecord = db.child("USER").child(user).get()
        userRecord = userRecord.val()

        userName = userRecord.get('NAME')
        userType = userRecord.get('TYPE')

        classUserAttentivenessObj = {
            "CLASS": classCode,
            "USER": user,
            "USER_NAME": userName,
            "ATTENTIVENESS" : attentiveness,
            "DATE" : str(today),
            "USER_TYPE" : userType
        }
        return classUserAttentivenessObj
    
