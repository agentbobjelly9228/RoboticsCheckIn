
# ccaroboticselective@gmail.com
# RoboticsCheckIn123$
import sys
import numpy as np
import os
import time
import PyQt5.sip
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QSizePolicy, QGridLayout, QPushButton, QMainWindow
from PyQt5.uic import loadUi
import json
import numpy as np5
from pyzbar.pyzbar import decode
from datetime import datetime, timedelta
from datetime import date
from datetime import timedelta
import pygame
import csv
import cv2
from filestack import Client
import _tkinter
import matplotlib.pyplot as plt
fig = plt.figure()
# assert 'QTAgg' in fig.canvas.__class__.__name__

pygame.init()
def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
class CheckIn(QMainWindow):
    people = ""
    csv_columns = ['ID','Name','Start', 'End', 'Total', 'Day']
    file = open('students.csv')
    reader = csv.reader(file)
    ids = {}
    c = Client("AoHueAVZ9Rm2ezM0xE7hTz")
    for row in reader:
        ids[row[0]] = row[1]
        # self.data = [
        #   {'ID': 10736, 'Name': 'Nathan Man', 'Start': 0, 'End': 0, 'Total': 0},
        #   {'ID': 10859, 'Name': 'self.data Yu', 'Start': 0, 'End': 0, 'Total': 0}
        # ]
    data = []
    f = open('files.json')
    files = json.load(f)['files']

    def __init__(self):
        super(CheckIn, self).__init__()
        loadUi(resource_path('signinUI.ui'), self)
        self.camera.clicked.connect(self.checkinCam)
        self.save.clicked.connect(self.saveFile)
        self.submit.clicked.connect(self.checkinNum)

    def checkinCam(self):
        dt = datetime.now()
        x = dt.weekday()
        print('it worked')
        for i in range(100):
            try:
                cap = cv2.VideoCapture(i)
                break
            except:
                if i >= 99:
                    print('no camera found')
                    return
                continue
                
        while True:
            print('hi')
            ret, frame = cap.read()
            frame = frame[0:3000, 0:4000, :]
            image_np = np.array(frame)
            detectedBarcodes = decode(image_np)
            
            # If not detected then print the message
            if not detectedBarcodes:
                pass
            else:
                # Traverse through all the detected barcodes in image
                barcode = detectedBarcodes[0]
                
                # Locate the barcode position in image
                (x, y, w, h) = barcode.rect
                
                # Put the rectangle in image using
                # cv2 to heighlight the barcode
                cv2.rectangle(image_np, (x-10, y-10),
                            (x + w+10, y + h+10),
                            (255, 0, 0), 2)
        
                if barcode.data!="":
                
                # Print the barcode self.data
                    # print(str(barcode.self.data))
                    idnum = str(barcode.data)[2:-1]
                    print(idnum)
                    time.sleep(2)
                    now = datetime.now()

                    current_time = now.strftime("%H:%M:%S")
                    print(current_time)
                    checkedIn = False
                    for i in range(len(self.data)):
                        if self.data[i]['ID'] == int(idnum):
                            checkedIn = True
                    if not checkedIn:
                        x = dt.weekday()
                        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                        self.data.append({'ID': int(idnum), 'Name': self.ids[idnum], 'Start': 0, 'End': 0, 'Total': 0, 'Day': days[x]})
                    print(self.data)
                    for i in range(len(self.data)):
                        if self.data[i]['ID'] == int(idnum):
                            ind = i
            
                    if self.data[ind]['Start'] != 0:
                        startTime = self.data[ind]['Start']
                        startTime = datetime.strptime(startTime, "%H:%M:%S")
                        current_time = datetime.strptime(current_time, "%H:%M:%S")
                        timeSpent = current_time - startTime
                        secondsSpent = int(timeSpent.total_seconds())
                        print(secondsSpent)

                        if secondsSpent < 600:
                            print('cant sign out too little time')
                            sound = pygame.mixer.Sound(resource_path("wrong.mp3"))
                            pygame.mixer.Sound.play(sound)
                            pygame.mixer.music.stop()
                            cap.release()
                            cv2.destroyAllWindows()
                            return
                        else:
                            sound = pygame.mixer.Sound(resource_path("sound.wav"))
                            pygame.mixer.Sound.play(sound)
                            pygame.mixer.music.stop()
                            print('goodbye')
                            self.data[ind]['End'] = current_time.strftime("%H:%M:%S")
                            formattedTimeSpent = str(timedelta(seconds=secondsSpent))
                            self.data[ind]['Total'] = formattedTimeSpent
                            cap.release()
                            cv2.destroyAllWindows()
                            return
                    else:
                        sound = pygame.mixer.Sound(resource_path("sound.wav"))
                        pygame.mixer.Sound.play(sound)
                        pygame.mixer.music.stop()
                        self.data[ind]['Start'] = current_time
                        print('welcome student #', idnum)
                        print('hi')
                        cap.release()
                        cv2.destroyAllWindows()
                        return
                    print('current students', self.data)
            cv2.imshow('object detection', image_np)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                return
    def checkinNum(self):
        dt = datetime.now()
        x = dt.weekday()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        print('it worked')
        if self.IDInput.toPlainText():
            
        # Print the barcode self.data
            # print(str(barcode.self.data))
            idnum = self.IDInput.toPlainText()
            print(idnum)
            time.sleep(2)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            checkedIn = False
            for i in range(len(self.data)):
                if self.data[i]['ID'] == int(idnum):
                    if self.data[i]['Day'] == days[x]:
                        checkedIn = True
                    else:
                        continue
            if not checkedIn:
                x = dt.weekday()
                days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                self.data.append({'ID': int(idnum), 'Name': self.ids[idnum], 'Start': 0, 'End': 0, 'Total': 0, 'Day': days[x]})
            print(self.data)
            for i in range(len(self.data)):
                if self.data[i]['ID'] == int(idnum):
                    ind = i

            if self.data[ind]['Start'] != 0:
                startTime = self.data[ind]['Start']
                startTime = datetime.strptime(startTime, "%H:%M:%S")
                current_time = datetime.strptime(current_time, "%H:%M:%S")
                timeSpent = current_time - startTime
                secondsSpent = int(timeSpent.total_seconds())
                print(secondsSpent)

                if secondsSpent < 600:
                    print('cant sign out too little time')
                    sound = pygame.mixer.Sound(resource_path("wrong.mp3"))
                    pygame.mixer.Sound.play(sound)
                    pygame.mixer.music.stop()
                else:
                    sound = pygame.mixer.Sound(resource_path("sound.wav"))
                    pygame.mixer.Sound.play(sound)
                    pygame.mixer.music.stop()
                    print('goodbye')
                    self.data[ind]['End'] = current_time.strftime("%H:%M:%S")
                    formattedTimeSpent = str(timedelta(seconds=secondsSpent))
                    self.data[ind]['Total'] = formattedTimeSpent
                    
            else:
                sound = pygame.mixer.Sound(resource_path("sound.wav"))
                pygame.mixer.Sound.play(sound)
                pygame.mixer.music.stop()
                self.data[ind]['Start'] = current_time
                print('welcome student #', idnum)
                
            print('current students', self.data)

    def saveFile(self):
        dt = datetime.now()
        x = dt.weekday()

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if days[x] == 'Tuesday':
            csv_file = 'week ending ' + days[x] + " " + str(dt.date()) + '.csv'
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                    writer.writeheader()
                    for datas in self.data:
                        writer.writerow(datas)
                with open('files.json', 'r+') as f:
                    dataFiles = json.load(f)
                    dataFiles['files'].append(csv_file)
                    f.seek(0)        
                    json.dump(dataFiles, f, indent=4)
                    f.truncate() 
                filelnk = self.c.upload(filepath = csv_file)
                exit()
                # need to update json
            except IOError:
                print("I/O error")
        else:
            # testData = [{'ID': int(10000), 'Name': 'Bob', 'Start': 0, 'End': 0, 'Total': 0, 'Day': 'Tuesday'}, {'ID': int(20000), 'Name': 'Bob', 'Start': 0, 'End': 0, 'Total': 0, 'Day': 'Tuesday'}]
            prev_file = csv.reader(open(self.files[-1]))
            prev_data = []
            for row in prev_file:
                if len(row) != 6:
                    continue
                prev_data.append({'ID': row[0], 'Name': row[1], 'Start': row[2], 'End': row[3], 'Total': row[4], 'Day': row[5]})
            prev_data = prev_data[1:]
            totalData = prev_data + self.data
            print(totalData)
            csv_file = self.files[-1]
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                    writer.writeheader()
                    for datas in totalData:
                        writer.writerow(datas)
                # filelnk = c.upload(filepath = csv_file)
                exit()
            except IOError:
                print("I/O error")

    def BarcodeReader(self, image):
     
        # read the image in numpy array using cv2
        img = cv2.imread(image)
        
        # Decode the barcode image
        detectedBarcodes = decode(img)
        
        # If not detected then print the message
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
        else:
        
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes: 
            
                # Locate the barcode position in image
                (x, y, w, h) = barcode.rect
                
                # Put the rectangle in image using
                # cv2 to heighlight the barcode
                cv2.rectangle(img, (x-10, y-10),
                            (x + w+10, y + h+10),
                            (255, 0, 0), 2)
                
                if barcode.data!="":
                
                # Print the barcode self.data
                    print(str(barcode.data))
                    print(barcode.type)
                    idnum = str(barcode.data)[2:-1]
                    print(idnum)
                    
        #Display the image
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# https://forms.office.com/r/jeNcmjj9R2
if __name__ == "__main__":
    app = QApplication([])
    widget = CheckIn()
    widget.show()
    sys.exit(app.exec_())
