import json
import io
import os
from Lib.FirebaseConnection import *

def getJsonData():
    FOLDER_PATH = r'resources'
    FILE_NAME = "CLASS_ATTENTIVENESS.json"
    with io.open(os.path.join(FOLDER_PATH, FILE_NAME), "rb") as file:
        content = file.read()

    # parse file
    obj = json.loads(content)
    print(obj['CLASS_ATTENTIVENESS'])
    # Closing file
    file.close()
    return obj['CLASS_ATTENTIVENESS']

def main():
    db = getFirebaseDb()
    dataList = getJsonData()
    for i in dataList:
        db.child('CLASS_ATTENTIVENESS').child(i['CLASS']+'_'+i['USER']).set(i)


if __name__ == '__main__':
    main()
