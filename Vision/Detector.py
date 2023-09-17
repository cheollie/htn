import cv2
import numpy as np
import time
import pyttsx3


class Detector:
    def __init__(self, videoPath, configPath, modelPath, classesPath):
        self.videoPath = videoPath
        self.configPath = configPath 
        self.modelPath = modelPath
        self.classesPath = classesPath
        self.net = cv2.dnn_DetectionModel(self.modelPath, self.configPath)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.net.setInputSize(320, 320)
        self.net.setInputScale (1.0/127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwapRB (True)
        self.object_timestamps = {}
        self.object_duration = {}
        self.readClasses()
        self.engine = pyttsx3.init()
    def readClasses(self):
        with open(self.classesPath, 'r') as f: self.classesList = f.read().splitlines()
        self.classesList.insert(0, '__Background__')
        print(self.classesList)
    def onVideo(self):
        cap = cv2.VideoCapture(self.videoPath)
        if (cap.isOpened()==False): 
            print("Error opening file...") 
            return
        last_time = time.time()
        (success, image) = cap.read()
        while success:
            classLabelIDs, confidences, bboxs = self.net.detect (image, confThreshold = 0.4)
            bboxs = list(bboxs)
            confidences = list(np.array(confidences).reshape(1,-1)[0])
            confidences = list(map (float, confidences))
            bboxIdx = cv2.dnn. NMSBoxes (bboxs, confidences, score_threshold = 0.35, nms_threshold = 0.2)
            """
            classLabel = self.classesList[classLabelID]
            displayText = "{}:{:.4f}".format(classLabel, classConfidence)
            x, y, w, h = bbox
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 255, 255), thickness=1)
            cv2.putText(image, displayText, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
            """

            if len(bboxIdx) != 0:
                for i in range(0, len(bboxIdx)):
                    bbox = bboxs [np. squeeze (bboxIdx[i])]
                    classConfidence = confidences [np. squeeze (bboxIdx[i])]
                    classLabelID = np. squeeze (classLabelIDs [np.squeeze (bboxIdx[i])])
                    classLabel = self.classesList[classLabelID]
                    displayText = "{}:{:.4f}".format(classLabel, classConfidence)
                    x,y,w,h = bbox
                    cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,255,255), thickness=1)
                    cv2.putText(image, displayText, (x,y-10), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
                    object_id = f"{classLabel}_{i}"
                    if object_id not in self.object_timestamps:
                        self.object_timestamps[object_id] = time.time()
                        self.object_duration[object_id] = 0
                    else:
                        self.object_duration[object_id] = time.time() - self.object_timestamps[object_id]  
                        if (int(self.object_duration[object_id]*10) % 100 == 0) and int(self.object_duration[object_id]) > 0:
                            print(f"{object_id} has been in frame for {self.object_duration[object_id]} seconds") 
                            self.engine.say(f"{object_id} has been in frame for {int(self.object_duration[object_id])} seconds")
                            self.engine.runAndWait()
            #"""
            #if time.time() - last_time >= 10:
            #    print(self.object_duration)
            #    print(sorted([(k,v) for k,v in self.object_duration.items()],key = lambda x: x[1]))
            #    last_time = time.time()
            #"""
            cv2.imshow("Result", image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            (success, image) = cap.read()
        cv2.destroyAllWindows()
        print()
        print(self.object_timestamps)
