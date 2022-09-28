from os import times
import time
from tracemalloc import start
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from datetime import datetime, timedelta
from datetime import date
from datetime import timedelta
import threading
import csv
import json
from playsound import playsound
import pygame
from filestack import Client
c = Client("AoHueAVZ9Rm2ezM0xE7hTz")

pygame.init()
csv_columns = ['ID','Name','Start', 'End', 'Total', 'Day']
file = open('students.csv')
reader = csv.reader(file)
ids = {}
for row in reader:
  ids[row[0]] = row[1]
# data = [
#   {'ID': 10736, 'Name': 'Nathan Man', 'Start': 0, 'End': 0, 'Total': 0},
#   {'ID': 10859, 'Name': 'Jay Yu', 'Start': 0, 'End': 0, 'Total': 0}
# ]
data = []
f = open('files.json')
files = json.load(f)['files']
# print(files)
dt = datetime.now()
x = dt.weekday()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

csv_file = days[x] + " " + str(dt.date())
print(csv_file)

def save():
  dt = datetime.now()
  x = dt.weekday()

  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if days[x] == 'Friday':
    csv_file = 'week starting ' + days[x] + " " + str(dt.date()) + '.csv'
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for datas in data:
                writer.writerow(datas)
        filelnk = c.upload(filepath = csv_file)
        exit()
        # need to update json
    except IOError:
        print("I/O error")
  else:
    # testData = [{'ID': int(10000), 'Name': 'Bob', 'Start': 0, 'End': 0, 'Total': 0, 'Day': 'Tuesday'}, {'ID': int(20000), 'Name': 'Bob', 'Start': 0, 'End': 0, 'Total': 0, 'Day': 'Tuesday'}]
    prev_file = csv.reader(open(files[-1]))
    prev_data = []
    for row in prev_file:
      prev_data.append({'ID': row[0], 'Name': row[1], 'Start': row[2], 'End': row[3], 'Total': row[4], 'Day': row[5]})
    prev_data = prev_data[1:]
    totalData = prev_data + data
    print(totalData)
    csv_file = files[-1]
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for datas in totalData:
                writer.writerow(datas)
        # filelnk = c.upload(filepath = csv_file)
        exit()
    except IOError:
        print("I/O error")
# save()
# exit()
delay = (datetime.combine(date.today() + timedelta(days=0), datetime.strptime('22:00:00', "%H:%M:%S").time()) - datetime.now()).total_seconds()
print(delay)
threading.Timer(delay, save).start()
# data = {
#   10736: {
#     'name': 'Nathan Man',
#     'start': 0,
#     'end': 0,
#     'total': 0
#   },
#   10859: {
#     'name': 'Jay Yu',
#     'start': 0,
#     'end': 0,
#     'total': 0
#   }
# }
# Make one method to decode the barcode
def BarcodeReader(image):
     
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
               
            # Print the barcode data
                print(str(barcode.data))
                print(barcode.type)
                idnum = str(barcode.data)[2:-1]
                print(idnum)
                 
    #Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
  # Take the image from user
    # image="barcode2.JPG"
    # BarcodeReader(image)
    cap = cv2.VideoCapture(0)
    while True:
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
            
            # Print the barcode data
                # print(str(barcode.data))
                idnum = str(barcode.data)[2:-1]
                print(idnum)
                time.sleep(2)
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print(current_time)
                checkedIn = False
                for i in range(len(data)):
                  if data[i]['ID'] == int(idnum):
                    checkedIn = True
                if not checkedIn:
                  x = dt.weekday()
                  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                  data.append({'ID': int(idnum), 'Name': ids[idnum], 'Start': 0, 'End': 0, 'Total': 0, 'Day': days[x]})
                for i in range(len(data)):
                  if data[i]['ID'] == int(idnum):
                    ind = i
                    sound = pygame.mixer.Sound("sound.wav")
                    pygame.mixer.Sound.play(sound)
                    pygame.mixer.music.stop()
                
                if data[ind]['Start'] != 0:
                  startTime = data[ind]['Start']
                  startTime = datetime.strptime(startTime, "%H:%M:%S")
                  current_time = datetime.strptime(current_time, "%H:%M:%S")
                  timeSpent = current_time - startTime
                  secondsSpent = int(timeSpent.total_seconds())
                  print(secondsSpent)
                
                  if secondsSpent < 10:
                    print('cant sign out too little time')
                  else:
                    print('goodbye')
                    data[ind]['End'] = current_time.strftime("%H:%M:%S")
                    formattedTimeSpent = str(timedelta(seconds=secondsSpent))
                    data[ind]['Total'] = formattedTimeSpent

                else:
                  data[ind]['Start'] = current_time
                  print('welcome student #', idnum)
                print('current students', data)
      cv2.imshow('object detection', image_np)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

