import requests,zipfile,io,subprocess,os,time,pathlib,urllib,sys,threading,pyfiglet
from elevate import elevate
#----------------------------------------------------------x-----------------------------------------------------------#
def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls')  
    else: 
        _ = os.system('clear') 
#----------------------------------------------------------x-----------------------------------------------------------#
def lineMarker(maxMarker):
	print("\t\t",end=" ")
	for i in range(0,maxMarker):
		print("-",end="")

def tabs(maxtabs):
	retab = ""
	for i in range(0,maxtabs):
		retab = retab + "\t"

	return retab
#----------------------------------------------------------x-----------------------------------------------------------#
def FirstScreen():
	print(pyfiglet.figlet_format("   8051SIM",font="nancyj-fancy"))
	print(tabs(9)+"- By rdeka"+"\n",end=" ")
	lineMarker(73)
	print("\n"+tabs(2)+" Not For Commercial uses, all rights are reversed under the Electronics &")
	print(tabs(2)+" Communication Department of University Of Engineering And Management, Kolkata")
	lineMarker(73)
#----------------------------------------------------------x-----------------------------------------------------------#
def LoadingScreen():
    loading_bar = []
    dashes = 1
    spaces = 10
    count = 0
    for i in range(25):
        print("Downloading : [",end="")
        for x in range(dashes):
            print("█",end="")
        for y in range(spaces):
            print(end=" ")
        time.sleep(1)
        clear()
        dashes += 1
        spaces -= 1
        count += 4
        print("] ", count, "%")
#----------------------------------------------------------x-----------------------------------------------------------#
def is_internet_available():
	try:
		urllib.request.urlopen('http://google.com',timeout = 1)
		return True
	except:
		return False
#----------------------------------------------------------x-----------------------------------------------------------#
#----------------------------------------------------------x-----------------------------------------------------------#
def StartProgExe(command):
	executionCommand = command.split()
	subprocess.call(executionCommand)
	time.sleep(2)
#----------------------------------------------------------x-----------------------------------------------------------#
#----------------------------------------------------------x-----------------------------------------------------------#	
def ReturnProgExeCode(command):
	FNULL = open(os.devnull,'w')
	executionCommand = command.split()
	retcode = subprocess.call(executionCommand,stdout = FNULL,stderr = subprocess.STDOUT)
	return retcode
#----------------------------------------------------------x-----------------------------------------------------------#
clear()
FirstScreen();
input("\n\t\t\tPress ENTER To Continue........")
#----------------------------------------------------------x-----------------------------------------------------------#
if is_internet_available() is True and pathlib.Path("edsim51di").exists() == False:
	LoadingScreen();
	r = requests.get("https://www.edsim51.com/8051simulator/edsim51di.zip")
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
elif is_internet_available() is False and pathlib.Path("edsim51di").exist() is False:
	print("PLEASE RETRY USING AN ACTIVE INTERNET CONNECTION....")
else:
	print("SKIPPING DOWNLOAD, FILE ALREADY EXISTS....")
#----------------------------------------------------------x-----------------------------------------------------------#
clear()
#----------------------------------------------------------x-----------------------------------------------------------#
try:
	ReturnProgExeCode("java -version")
except FileNotFoundError:
	print("Java is not installed in this system,Initiating java install....")
	print("\n*PLEASE RE-RUN THIS PROGRAM ONCE INSTALLATION COMPLETES*")
	elevate(show_console = False, graphical=False)
	TheadObjectWin = threading.Thread(target=subprocess.Popen(['JavaSetup8u251.exe']))
	ThreadObjectWin.start()
	ThreadObejctWin.join()
else:
	StartProgExe("java -jar edsim51di/edsim51di.jar") if sys.platform == "linux" else StartProgExe("java -jar edsim51di\\edsim51di.jar")
#----------------------------------------------------------x-----------------------------------------------------------#
