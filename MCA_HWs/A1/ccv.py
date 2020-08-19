import numpy as np
import cv2
from PIL import Image 
import os
import matplotlib.pyplot as plt

def create_ccv():
	path = os.path.join("images")
	os.chdir(path)
	ccv_list = []
	i = 0
	for img in os.listdir(os.getcwd()):
		print(i)
		name = img
		img = cv2.imread(img,0)
		histg = cv2.calcHist([img],[0],None,[256],[0,256])
		ccv_list.append((histg,name))
		i+=1
		
	os.chdir("..")
	with open("ccv.txt",'w') as file:
		for item in ccv_list:
			file.write(item[1])
			file.write(" ")
			for k in range(256):
				file.write(str(item[0][k][0]))
				file.write(" ")
			file.write("\n")

def query():
	path = os.path.join("train","query")
	os.chdir(path)
	for query in os.listdir(os.getcwd()):
		print(acc)
		with open(query,'r') as q:
			img = q.read()
			img = img.split()
			img = img[0][5:]
			img = img+".jpg"
			print(img)

		os.chdir("..")
		os.chdir("..")
		with open("ccv.txt",'r') as img_ccv:
			ccv = img_ccv.readlines()
			ind = 0
			for i in range(len(ccv)):
				ccv[i] = ccv[i].split()
				name = ccv[i][0]
				if(img == name):
					ind = i 
					break

			retrive(ind)
			print(ind)

		break

def change(lt):
	for i in range(len(lt)):
		lt[i] = float(lt[i])
	return lt

def compute(lt,query):
	s = 0
	for i in range(len(query)):
		s+=abs(lt[i]-query[i])
	return s/256

def sort_list(lt):  
    lt.sort(key = lambda x: x[0])  
    return lt

def show(final):
	for i in range(3):
		with open("ccv.txt",'r') as file:
			lines = file.readlines()
		ind = final[i][1]
		lines[ind] = lines[ind].split()
		img = lines[ind][0]
		path = os.path.join("images",img)
		img = Image.open(path)
		img.show()


def retrive(ind):

	final = []
	with open("ccv.txt") as file:
		ccv = file.readlines()

		query = ccv[ind].split()
		q_img = query[0]
		query.pop(0)
		query = change(query)

		path = os.path.join("images",q_img)
		q_img =Image.open(path)
		q_img.show()


		for i in range(len(ccv)):
			ccv[i] = ccv[i].split()
			ccv[i].pop(0)
			ccv[i] = change(ccv[i])
			val = compute(ccv[i],query)
			final.append((val,i))
	
	sorted_final = sort_list(final)
	
	show(sorted_final)



#create_ccv()
query()