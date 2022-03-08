import requests,zipfile,io,subprocess,os,time,pathlib,urllib,sys,threading,pyfiglet,shutil
#----------------------------------------------------------x-----------------------------------------------------------#
#----------------------------------------------------------x-----------------------------------------------------------#
def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls')  
    else: 
        _ = os.system('clear') 
	
def tabs(maxtabs):
    retab = ""

    for i in range(0,maxtabs):
        retab = retab + "\t"

    return retab

def lineMarker(maxMarker):

    print(tabs(2),end=" ")

    for i in range(0,maxMarker):
        print("-",end="")

def FirstScreen():
    print(pyfiglet.figlet_format("   8051SIM", font = "nancyj-fancy"))
    print(pyfiglet.figlet_format("     GUIDE", font = "nancyj-fancy"))
    print(tabs(9)+"-rdeka"+"\n",end=" ")
    lineMarker(73)
    print("\n"+tabs(2)+" Not For Commercial use, all rights are reversed under the Electronics &")
    print(tabs(2)+" Communication Department of University Of Engineering And Management,Kolkata")
    lineMarker(73)

def DownloadingScreen():
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

def dprint(text):
    print("\n")
    lineMarker(73)
    print("\n"+tabs(3)+text)
    lineMarker(73)
    print("\n")
#----------------------------------------------------------x-----------------------------------------------------------#
def CreateNewFolder(folderName):
    directory = folderName
    parent_dir = os.path.abspath(os.getcwd())
    path = os.path.join(parent_dir,directory)
    try:
        os.mkdir(path)
    except FileExistsError:
        print("File Already Exists!")
        exit(1)
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

def DownloadProgram(url):
	r = requests.get(url)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
#----------------------------------------------------------x-----------------------------------------------------------#
clear()
FirstScreen();
input("\n"+tabs(3)+"Press ENTER To Continue........")
#----------------------------------------------------------x-----------------------------------------------------------#
#----------------------------------------------------------x-----------------------------------------------------------#
if is_internet_available() is True and pathlib.Path("StuffYouShouldNeverCare\\edsim51di").exists() is False:
    ThreadObjWin32 = threading.Thread(target = DownloadProgram,args = ["https://www.edsim51.com/8051simulator/edsim51di.zip"])
    ThreadObjWin32.start()
    DownloadingScreen()
    ThreadObjWin32.join()
    CreateNewFolder('StuffYouShouldNeverCare')
    shutil.move("edsim51di", "StuffYouShouldNeverCare")	
elif is_internet_available() is False and pathlib.Path("StuffYouShouldNeverCare\\edsim51di").exists() is False:
	dprint("PLEASE RETRY USING AN ACTIVE INTERNET CONNECTION....")
	clear()
	exit(1)
else:
	clear()
	dprint("SKIPPING DOWNLOAD, FILE ALREADY EXISTS....")
#----------------------------------------------------------x-----------------------------------------------------------#
#----------------------------------------------------------x-----------------------------------------------------------#
try:
	StartProgExe('java -version')
except FileNotFoundError:
    if pathlib.Path("StuffYouShouldNeverCare\\jdk-13").exists() is False and is_internet_available() is True:
        dprint("Java is not installed in this system,Initiating Java install....")
        ThreadObjWin32 = threading.Thread(target = DownloadProgram,args = ["https://download.java.net/openjdk/jdk13/ri/openjdk-13+33_windows-x64_bin.zip"])
        ThreadObjWin32.start()
        DownloadingScreen()
        ThreadObjWin32.join()
        shutil.move("jdk-13", "StuffYouShouldNeverCare")
        subprocess.Popen(['set','PATH=%cd%\\StuffYouShouldNeverCare\\jdk-13\\bin;%PATH%'],shell=True)
        StartProgExe("java -jar StuffYouShouldNeverCare/edsim51di/edsim51di.jar") if sys.platform == "linux" else StartProgExe("java -jar StuffYouShouldNeverCare\\edsim51di\\edsim51di.jar")
        exit(1)
    elif pathlib.Path("StuffYouShouldNeverCare\\jdk-13").exists() is True:
        subprocess.Popen(['set','PATH=%cd%\\StuffYouShouldNeverCare\\jdk-13\\bin;%PATH%'],shell=True)
        StartProgExe("java -jar StuffYouShouldNeverCare/edsim51di/edsim51di.jar") if sys.platform == "linux" else StartProgExe("java -jar StuffYouShouldNeverCare\\edsim51di\\edsim51di.jar")
        exit(1)
    else:
        dprint("PLEASE RETRY USING AN ACTIVE INTERNET CONNECTION....")
else:
	StartProgExe("java -jar StuffYouShouldNeverCare/edsim51di/edsim51di.jar") if sys.platform == "linux" else StartProgExe("java -jar StuffYouShouldNeverCare\\edsim51di\\edsim51di.jar")
#----------------------------------------------------------x-----------------------------------------------------------#
