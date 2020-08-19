import numpy as np
import matplotlib.pyplot as plt
import os 
from scipy.io import wavfile

def compute_spectrogram():

	path = os.path.join("training")
	numbers = os.listdir(path)
	try:
		numbers.remove('.DS_Store')
	except:
		pass
	print(numbers)
	print(path)
	for number in numbers:
		audios = os.listdir(os.path.join(path,number))
		try:
			audios.remove('.DS_Store')
		except:	
			pass

		for audio in audios:
			samplingFrequency, signalData = wavfile.read(os.path.join(path,number,audio))
			a = spectrogram(signalData,samplingFrequency)
			
			break
		break
		

def spectrogram(data,freq):
	size = 40
	overlap = 20
	start = 0
	segment_fft = []
	while(start+20<=16000):

		segment = data[start:start+20]
		segment_fft.append(np.fft.fft(segment))
		start+=100
	arr = np.array(segment_fft,dtype = float).T
	print(arr.shape)
	plot(arr)
	return segment_fft

def plot(arr):
	plt.figure(figsize = (8,8))
	
	
	plt.imshow(arr)

	plt.colorbar()
	plt.show()






compute_spectrogram()







