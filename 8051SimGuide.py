import progressbar

import urllib.request
import os
from sys import platform, maxsize
from zipfile import ZipFile

_WIN = os.name == "nt"

OS = "windows" if _WIN else platform
ARCH = "x64" if maxsize > 2**32 else "x86"


def greeting():
    print(r"""
   ___   ___  _____ __  _____ _            _____       _     _      
  / _ \ / _ \| ____/_ |/ ____(_)          / ____|     (_)   | |     
 | (_) | | | | |__  | | (___  _ _ __ ___ | |  __ _   _ _  __| | ___ 
  > _ <| | | |___ \ | |\___ \| | '_ ` _ \| | |_ | | | | |/ _` |/ _ \
 | (_) | |_| |___) || |____) | | | | | | | |__| | |_| | | (_| |  __/
  \___/ \___/|____/ |_|_____/|_|_| |_| |_|\_____|\__,_|_|\__,_|\___|
                                                                    
    """)
    input("HIT ENTER to continue")

class customProgressBar:
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):

        if not self.pbar:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


def getDwnURL(os: str = OS, arch: str = ARCH, mode: int = 1) -> str:
    lurl = [
        f"https://cdn.azul.com/zulu/bin/zulu17.38.21-ca-jre17.0.5-{os}_{arch}.zip",
        f"http://www.edsim51.com/8051simulator/edsim51di.zip",
    ]

    return lurl[0] if mode == 1 else lurl[1]


def dwnUFn(url, filename):
    urllib.request.urlretrieve(url, filename, customProgressBar())


def buildDir():
    if OS == "linux":
        os.makedirs(".data", exist_ok=True)
    else:
        os.makedirs("data/", exist_ok=True)
        os.system("attrib +h data")


def unzip(filename):
    with ZipFile(filename, "r") as zip:
        zip.printdir()
        zip.extractall()


def _task(Filename, mode):
    URL = getDwnURL(mode=mode)
    dwnUFn(URL, Filename)
    unzip(Filename)
    os.system(f"rm -rf {Filename}")
    Filename = Filename[0:-4]
    os.system(f"mv {Filename} .data/")


def main():
    os.system("clear")
    greeting()
    buildDir()
    command = ""
    _filename = f"zulu17.38.21-ca-jre17.0.5-{OS}_{ARCH}"
    _efilename = "edsim51di"

    if os.system("ls .data/edsim51di") == 0:
        print(f"{_efilename} already configured")
    else:
        print("Getting edsim51 ready!")
        _task(_efilename + ".zip", 2)

    if os.system("java --version") != 0:
        if os.system(f"ls .data/{_filename}") == 0:
            print(f"{_filename} found, skipping")
        else:
            print("Getting Java Run Time")
            _task(_filename + ".zip", 1)

        if OS == "linux":
            os.system(f"chmod +x .data/{_filename}/bin/java")

        command = (
            f"./.data/{_filename}/bin/java -jar .data/{_efilename}/{_efilename}.jar"
        )
    else:
        command = f"java -jar .data/{_efilename}/{_efilename}.jar"

    os.system(command)
    os.system("rm -rf *.ser")

main()
