import os
try:
	from PIL import Image, ExifTags
except Exception, e:
	os.system("sudo apt install python-pil*")
try:
	import pyPdf, pdftools
except Exception, e:
	os.system("sudo apt install python-pyPdf, pdftools")
import sys
from time import *
import subprocess
from threading import *
import traceback
import platform
import hashlib
from random import *
import zipfile
import rarfile


W = '\033[0m' # White / Reset
BO = '\033[1m' # Bold
UN = '\033[4m' # Underline
C = '\033[36m' # Cyan
B, R, Y, G = '\33[94m', '\033[91m', '\33[93m', '\033[1;32m' # Blue, Red, Yellow, Green


def main():
	# Sudo (Super User Do) check
	if not os.geteuid() == 0:
    		print (R + "Please start " + __file__ + " with sudo!")
		exit(0)
	# Checking for Linux
	if str(platform.system()) != "Linux":
    		print (G + "Please use " + __file__ + " only on Linux!")
	os.system("clear")

	print ""
	print('''{0}{1}
	      			 	###   ##       #     #####  #   #     ##    ##    ##     #  ##########  #####   ##   ##
	      			        #  #  ##      # #    #      # #        ##  ####  ##     # #     ##      ##      ##   ##
	     			      	###   ##     #   #   #      ##         ## # ## # ##    #   #    ##      ##      #######
					#  #  ##     #   #   #      # #         ##  ##  ##     #   #    ##      ##      ##   ##
					###   #####  #####   #####  #	#       ##  ##  ##     #####    ##  	#####   ##   ##	'''.format('\n' * 1, R))	#Picture

	sleep(1.5)
	print ""
	print ""
	print (G + "Welcome to BL4CK_W4TCH!")
	print ""
	print (G + "Please choose one Module...")
	print ""
	print (G + "[1] Metadata Analyzer")
	print ""
	print (G + "[2] Crypter")
	print ""
	print (G + "[3] Open Images etc.")
	print ""
	print (G + "[4] Change Metadata")
	print ""
	print (G + "[5] Delete all Metadata")
	print ""
	print (G + "[6] Desktop Changer")
	print ""
	print (G + "[7] Exit")
	print ""
	choose = input(R + "root@BW: " + W)
	
	if choose == 1:
		metadata()
	elif choose == 2:
		crypter()
	elif choose == 3:
		openImage()
	elif choose == 4:
		change()
	elif choose == 5:
		delete()
	elif choose == 6:
		desktop()
	elif choose == 7:
		os.system("clear")
		exit(0)
	else:
		print ""
		print (G + "Unknown command...")
		sleep(0.7)
		main()

def metadata():
	print ""
	print (G + "Welcome to the Metadata analyzing Module!")
	print ""
	print (G + "Please enter the module")
	print ""
	print (G + "[1] Picture")
	print ""
	print (G + "[2] Zip-File")
	print ""
	print (G + "[3] Rar-File")
	print ""
	print (G + "[4] PDF-File")
	print ""
	print (G + "[5] Back to main")
	def picture():
		print (G + "Please choose a picture")
		print ""
		os.system("ls *.jpg && ls *.png")
		openquest = raw_input(R + "root@BW: " + W)
		op = Image.open(openquest)
		if not os.path.isfile(openquest):
			print (G + "[-] File does not exist!")
			metadata()
		if not os.access(openquest, os.R_OK):
			print (G + "[-] Access denied!")
			metadata()
		exif = op._getexif()
        	try:
			for i, j in exif.items():
                		if i in ExifTags.TAGS:
                        		print (ExifTags.TAGS[i] + " - " + str(j))
		except Exception, e:
			print e#
	def zip():
		print (G + "Please choose a zip file")
		print ""
		openquest = raw_input(R + "root@BW: " + W)
		op = zipfile.ZipFile(openquest)
		if not os.path.isfile(op):
			print (G + "[-] File does not exist!")
			metadata()
		if not os.access(op, os.R_OK):
			print (G + "[-] Access denied!")
			metadata()
		print (G + "Not implemented yet!")

	def rar():
		print (G + "Please choose a rar file")
		print ""
		openquest = raw_input(R + "root@BW: " + W)
		op = rarfile.RarFile(openquest)
		if not os.path.isfile(op):
			print (G + "[-] File does not exist!")
			metadata()
		if not os.access(op, os.R_OK):
			print (G + "[-] Access denied!")
			metadata()
		print (G + "Not implemented yet!")

	def pdf():
		print (G + "Please choose a pdf file")
		print ""
		openquest = raw_input(R + "root@BW: " + W)
		op = pdf.PdF(openquest)
		if not os.path.isfile(op):
			print (G + "[-] File does not exist!")
			metadata()
		if not os.access(op, os.R_OK):
			print (G + "[-] Access denied!")
			metadata()
		print (G + "Not implemented yet!")
	print ""
	meta_input = input(R + "root@BW: " + W)
	if meta_input == 1:
		picture()
	elif meta_input == 2:
		zip()
	elif meta_input == 3:
		rar()
	elif meta_input == 4:
		pdf()
	elif meta_input == 5:
		main()
	else:
		print (G + "Unknown input...")
		sleep(0.7)
		main()

def crypter():
	print (Y + BO + "NOT FINISHED!")
	print ""
	print (G + "Welcome to the crypting Module")
	print ""
	sleep(0.7)
	print (G + "Please select the module!")
	print ""
	sleep(0.7)
	print (G + "[1] AES-256-ECB (Electric Code Block)")
	print ""
	sleep(0.7)
	print (G + "[2] AES-256-CCB")
	print ""
	print (G + "[3] Back to main")
	print ""
	mod_quest = input(R + "root@BW: " + W)	

	def ecb256():
		picq = raw_input(R + "PICTURE: " + W)
		pic = Image.open(picq)
		os.system("openssl aes-256-ecb --crypt " + pic)
	def ccb256():
		picq = raw_input(R + "PICTURE: " + W)
		pic = Image.open(picq)
		os.system("openssl aes-256-ccb --crypt " + pic)
	
	if mod_quest == 1:
		ecb256()
	elif mod_quest == 2:
		ccb256()
	elif mod_quest == 3:
		main()
	else:
		print "Unknown input"
		crypter() 

def openImage():
	print ""
	print (G + "Welcome to the opening Module!")
	print ""
	print (G + "Please enter the name of the file!")
	print ""
	sleep(0.7)
	openquest = raw_input(R + "root@BW: " + W)
	os.system("ls *.jpg && ls *.png")
	if not os.path.isfile(openquest):
		print "[-] File does not exist!"
		openImage()
	if not os.access(openquest, os.R_OK):
		print "[-] Access denied!"
		main()
	try:
		image = Image.open(openquest)
		image.show()
		main()
	except KeyboardInterrupt:
		main()

def change():
	print ""
	print (G + "Not implemented yet!")
	sleep(1.0)
	main()

def delete():
	print (Y + BO + "NOT FINISHED!")
	print ""
        print (G + "Welcome to the Metadata deleting Module!")
        print ""
        sleep(0.7)
        print (G + "Please enter the name of the file!")
        print ""
        sleep(0.7)
        openquest = raw_input(R + "root@BW: " + W)
        if not os.path.isfile(openquest):
                print (G + "[-] File does not exist!")
                delete()
        if not os.access(openquest, os.R_OK):
                print (G + "[-] Access denied!")
                main()
	try:
		try:
        		for i, j in Image.open(openquest)._getexif().items():
                		if i in ExifTags.TAGS:
					print ""
					print (G + "Do you want to delete the metadata? Y/N")
					print ""
					quest1 = raw_input(R + BO + "root@BW: " + W)
					if quest1 == "Y":
						for delete in (ExifTags.TAGS):
							try:
								_delete = delete._delexif().items() # Only an Experiment (_delexif())
							except Exception, e:
								print e
					elif quest1 == "N":
						main()
					else:
						print ""
						print (G + "Unknown input...")
						os.system("clear")
						main()
		except Exception, e:
			print e
	except KeyboardInterrupt:
		main()
def desktop():
	print ""
	print (G + "Welcome to the Desktop Module!")
	print ""
	try:
		print (G + "Please enter the name of the picture")
		question = raw_input(R + "root@BW: " + W)
		ask = raw_input(G + "Do want to change your Dextop Background to " + question + "? Y/N: " + W)
        	if (ask == "Y") | (ask == "y"):
                	if not os.path.isfile(question):
                        	print "File does not exist"
                	if not os.access(question, os.R_OK):
                        	print "Cannot access"
                	os.system('sudo feh --bg-scale ' + '"' + question + '"')
        	elif (ask == "N") | (ask == "n"):
                	main()
        	else:
                	print "Error"
                	main()
		main()
	except KeyboardInterrupt:
		main()


if __name__ == "__main__":
	main()
