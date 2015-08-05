#!/usr/bin/python
#!/usr/bin/bash
import os
import subprocess, shlex
from subprocess import Popen, PIPE


def count(filename):
	lines = 0
	for i in open(filename):
		lines += 1
	return lines

def repl(reemplazo, nuevo, filename):
	lector = open(filename , "r")
	arch = lector.read()
	arch = arch.replace(reemplazo, nuevo)
	escritor = open(filename, "w+")
	escritor.write(arch)
	escritor.close()
	return "Done Reemplazo"

def masscan(numeropuerto):
	#os.popen("sudo masscan -iL whitelist.csv -p"+numeropuerto+" -oX puerto"+numeropuerto+"_oman --rate 100").read()
	return "Done Masscan whitelist"

def versiones(numeropuerto):
	#lector = open("puerto"+str(numeropuerto)+".txt","r")
	#leyendo = lector.read()
	#guardado = filename+"version.txt"
	#lectorsito = open(guardado, "w+")
	for i in open("puerto"+str(numeropuerto)+".txt", 'a+b'):
		version = subprocess.call(["nc", "-n", "-w", "2", format(i), str(numeropuerto)])
		
		#echo = subprocess.call(['echo','-e', str(version),'>',"version"+str(numeropuerto)+".txt"],shell=True)
		echo = subprocess.call("echo -e" +str(version) ">> version"+str(numeropuerto)+".txt", shell=True)
		print echo


		#print version
		#lectorsito.write(str(version))
######## ACA VOYYY #########
		#ipversion = os.system(version)
		#print ipversion
	


if __name__ == "__main__":
	archivo = "ejemplo.txt"
	archivo2 = "latex.txt"	
	
	print count(archivo)

	print repl("HTTPPSCantidad", str(count(archivo)), archivo2)


####### Puertos #######

	for i in [21, 22, 23]:
		#### FTP - CONTROL ####
		if i == 21:
			#os.popen("sudo rm " "puerto"+str(i)+"_oman").read()
		
			#print masscan(str(i))
			#print filtrarxml(str(i))
			#filename = "puerto"+str(i)
			print versiones(i)
	

	

