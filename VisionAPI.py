import os
import json
import io
import time
from google.cloud import vision
from google.cloud.vision_v1 import AnnotateImageResponse
from google.cloud.vision_v1 import types


def startRecoding(seconds):

    #Connection Token
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'resources/Credentials/pass_key_ar.json'

    client = vision.ImageAnnotatorClient()
    FOLDER_PATH = r'resources'

    detectionConfidenceList = list()
    avgDetection = 0
    counter = 1
    
    while True:
        try:
            FILE_NAME = "pic.jpg"
            with io.open(os.path.join(FOLDER_PATH, FILE_NAME), "rb") as image_file:
                content = image_file.read()

            image = vision.Image(content=content)

            response = client.face_detection(image=image)
            
            response_json = AnnotateImageResponse.to_json(response)
            info = json.loads(response_json)
            
            if(info["faceAnnotations"] is not None and len(info["faceAnnotations"]) > 0):
                line = info["faceAnnotations"][0]
                   
                finalvalues = list(line.values())
                finalkeys = list(line.keys())

        ##        for i in range(-12,0):
        ##           print(i,finalkeys[i], ":", finalvalues[i])
                print('Mid work value check:',finalvalues[6])               
                detectionConfidenceList.append(finalvalues[6])

            else:
                print('Mid work value check:',0)
                detectionConfidenceList.append(0)

            if len(detectionConfidenceList) == 10:
                    avgDetection = sum(detectionConfidenceList)/10
                    break

        except IndexError as e:
            print("Oops!", e.__class__, "occurred.")
        except FileNotFoundError as e:
            print("Oops!", e.__class__, "occurred. Cannot read Image from the system.")
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        finally:
            if(counter == 10):
                break
            counter = counter + 1
            time.sleep(seconds)
            

    print('avgDetection', avgDetection)        
    return avgDetection

if __name__ == '__main__':
    startRecoding(.5)








