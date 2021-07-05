from PIL import ImageGrab
from datetime import datetime
import cv2
import pytesseract
import os
import psutil
from ctypes import windll
import win32gui
from imutils import contours
import numpy as np 
import argparse
import imutils
from PIL import Image
import joblib,cv2
import numpy as np
model = joblib.load("model/svm_5label_linear")
from PIL import ImageGrab
from PIL import Image
import time
from sklearn.preprocessing import MinMaxScaler
import csv
import pandas as pd
import glob
import serial
import serial.tools.list_ports as port_list

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\\tesseract.exe"

def send_data(search_channel):
	serialcomm = serial.Serial('COM5', 9600)

	serialcomm.timeout = 1
	time.sleep(1)
	serialcomm.write(search_channel.encode())


def  image_slice():
	im = Image.open("C:/Users/amo4clj/Desktop/Channel Digit Recognizer/Screen Shots/ocr_input_1.png")
	#im.show()
	ref = cv2.imread("C:/Users/amo4clj/Desktop/Channel Digit Recognizer/Screen Shots/ocr_input_1.png")
	ref = imutils.resize(ref, width=300)
	ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
	#ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
	ref = cv2.threshold(ref, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imwrite("C:/Users/amo4clj/Desktop/Channel Digit Recognizer/Screen Shots/converted_reference_image.png", ref)
	im = Image.open("C:/Users/amo4clj/Desktop/Channel Digit Recognizer/Screen Shots/converted_reference_image.png")
	#im.show()
	refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	refCnts = imutils.grab_contours(refCnts)
	refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]
	digits = {}
	for (i, c) in enumerate(refCnts):
		# compute the bounding box for the digit, extract it, and resize
		# it to a fixed size
		(x, y, w, h) = cv2.boundingRect(c)
		roi = ref[y:y + h, x:x + w]
		roi = cv2.resize(roi, (57, 88))
		# update the digits dictionary, mapping the digit name to the ROI
		fname = "C:/Users/amo4clj/Desktop/python/Screen Shots/pic_{}.png".format(str(i))
		cv2.imwrite(fname, roi)
		im = Image.open(fname)
		#im.show()
		digits[i] = fname
	del digits[0]	
	return(digits)	

def image_processing(digits):
	channels = {}
	for key,digit in digits.items():
		#print(digit)
		im = Image.open(digit)
		#im.show()
		im = cv2.imread(digit)
		im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)
		#print(im_gray)
		ret, im_th = cv2.threshold(im_gray, 100, 255, cv2.THRESH_BINARY)
		roi = cv2.resize(im_th, (28, 28), interpolation=cv2.INTER_AREA)
		rows,cols = roi.shape
		#print(rows)
		#print(cols)
		X=[]
		for i in range(rows):
			for j in range(cols):
				k = roi[i,j]
				if k > 100:
					k = 1
				else:
					k = 0
				X.append(k)
		
		predictions = model.predict([X])
		channels[key] = str(predictions)
	return(channels)

def string_manipulation(result):
		channels = []
		channels = list(result.values())
		for i in channels:
			channels = (''.join(channels))
			channels = channels.replace("[","")
			channels = channels.replace("]","")
			channels = channels.replace("'","")
			return(channels)

serialcomm = serial.Serial('COM5', 9600)

serialcomm.timeout = 1
channels_list = ['0']
while True:
	procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
	for i in procs:
		try:
			if "python" in procs[i]["name"]:
			
				digits = image_slice()
				result = image_processing(digits)
				channels = string_manipulation(result)
				channels = "s"+channels+"f"
				if (channels_list[-1] != channels):
					channels_list.append(channels)
					time.sleep(3)
					serialcomm.write(channels_list[-1].encode())
				else:
					f = open('input_channel/temp_file.txt','r+')
					input_channel = (f.read())	
					f.truncate(0)
					f.close()
					
				time.sleep(1)
				serialcomm.write(input_channel.encode())
				
		except:		
			pass		