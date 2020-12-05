from binascii import *
from PIL import Image, ImageDraw
import os
import math

userInput = input("Enter then name of the file you want: ")

f = open(userInput, "rb")

def getLengthOfFile():
	length = os.stat(userInput).st_size
	return length

def convertCharToBin(char):
	scale = 16
	text = hexlify(char)


	num_of_bits = 8

	binary = bin(int(text, scale))[2:].zfill(num_of_bits)
	return binary

file_length = getLengthOfFile()

dimension1 = file_length*8

dimension = math.ceil(math.sqrt(dimension1))

def getBinaryFromFile():
	bits = ''
	for char in f.read():
		asc = chr(char)
		binary = convertCharToBin(asc.encode("ascii"))
		bits += binary
	return bits

binaryOfFile = getBinaryFromFile()
print(binaryOfFile)
def createImage(dimension):
	img = Image.new('RGB', (dimension,dimension))
	for x in range(1,dimension):
		for y in range(1, dimension):
			if binaryOfFile[x*y] == "1":
				img.putpixel((x,y), (255,255,255))
			else:
				img.putpixel((x,y), (0,0,0))
	img.save("bitimage.png")

createImage(dimension)