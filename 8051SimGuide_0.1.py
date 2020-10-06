import requests
import os
from zipfile import ZipFile

from sys import platform, maxsize

_IS_WINDOWS = os.name == 'nt'

OS = 'windows' if _IS_WINDOWS else platform
ARCH = 'x64' if maxsize > 2**32 else 'x32'


class Implementation:

    OPENJ9 = 'openj9'
    HOTSPOT = 'hotspot'


def bytesToMb(a):
    return round(a / 1000000, 2)


def dowloadFile(file_name, link, header=None, show_output=True):
    r = requests.request('GET', link, headers=header, stream=True)
    f = open(file_name, 'wb')
    if file_name == "edsim51di.zip":
        size = 362273
    else:
        size = int(r.headers['Content-length'])
    sizet = 0
    for chunk in r.iter_content(chunk_size=8192):
        s = len(chunk)
        sizet += s
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
        status = round(sizet / size * 100, 3)
        if show_output:
            print('\r %.2f%% (%.2fMb/%.2fMb)' %
                  (status, bytesToMb(sizet), bytesToMb(size)),
                  end=' ',
                  flush=True)
    if show_output:
        print(" ")
    f.close()


def normalize_version(version: str) -> str:
    if version == '1.8':
        return '8'
    return version


def get_download_url(version: str,
                     operating_system: str = OS,
                     arch: str = ARCH,
                     impl: str = Implementation.HOTSPOT,
                     jre: bool = False) -> str:

    version = normalize_version(version)
    if jre:
        return f'https://api.adoptopenjdk.net/v3/binary/latest/{version}/ga/{operating_system}/{arch}/jre/{impl}/normal/adoptopenjdk'
    else:
        return f'https://api.adoptopenjdk.net/v3/binary/latest/{version}/ga/{operating_system}/{arch}/jdk/{impl}/normal/adoptopenjdk'


def downloadZipAndExtract(file_name, link, dir):
    dowloadFile(file_name, link)
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        print('Extracting the java files...')
        zip.extractall(dir)
        print('Java downloaded!')


os.makedirs('StuffYouShouldNeverCare', exist_ok=True)
java_command_index = 0
java_command = "java"

print("Checking java...")
if os.system(java_command + " -version") == 1:
    try:
        os.listdir("jdk")
    except:
        file_name = "jdk.zip"
        print('Java is missing.')
        print('Downloading the java files...')
        downloadZipAndExtract("jdk.zip", get_download_url('15'), "jdk")
        java_command = os.path.join("jdk", os.listdir("jdk")[0], "bin", "java")

if len(os.listdir("StuffYouShouldNeverCare")) == 0:
    print('8051simulator project files are missing.')
    print('Downloading the project files...')
    downloadZipAndExtract(
        "edsim51di.zip", "https://www.edsim51.com/8051simulator/edsim51di.zip",
        "StuffYouShouldNeverCare")

os.system(
    java_command + " -jar " +
    os.path.join("StuffYouShouldNeverCare", "edsim51di", "edsim51di.jar"))
