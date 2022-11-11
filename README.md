
# 8051SimGuide [UPDATE]

This project, rather this script, started off as a form of
help that I wanted to offer to my fellow University mates back during Engineering School.
We had a subject called Microcontrollers and Microprocessor (ECC403) in our curriculum. We had to deal with a
simulator which would simulate the working of 8051 Microcontroller. This emulator edsim51di was written in java.

And most of my peers found it difficult to run this piece of software as it was a jar file and required some command line tinkering.
As most programmers who are starting out, they were petrified from the command line. And did not know how they'd 
run this simulator. This is when, using the power of automation and my little knowledge of Operating System, I made the 8051SimGuide Script

UPDATE: November, 2022

At the time of writing, I was still a student and trying out different things to work on, so 
that I could improve on programming. Hence, after 2 years of the original script.
I learnt shell scripting using [bash shell](https://www.gnu.org/software/bash/).
Branch [v2](https://github.com/rd3ka/8051SimGuide/tree/v2) of this repository contains the new and improved script.



## Installation & Dependencies

This python script is 95% pure i.e does not use any external 
librabies expect for one, ['ProgressBar'](https://pypi.org/project/progressbar2/)

Master Branch:

To run the unpackaged script install via pip
```bash
  pip install progressbar2
```
If pip is not available, use easy
```bash
  easy_install progressbar2
```

v2 Branch:

**Linux** : The script was made using bash shell which is used in most
common distribution. ``` curl``` , ```tee```, ```ping```, ```zip``` and ```tar```
commands are used. These commands come preinstalled and are essential part of the kernel in most 
distributions.
In case, the script errors out:

```
Debain/Ubuntu : sudo apt-get -y install curl, tee, ping, tar
Arch :          sudo pacman -y -S curl, tee, ping, tar
Fedora/RedHat : sudo dnf -y install curl, tee, ping, tar
```
Before running the script don't forget to change the execution group/policy
```
  chmod +x 8051SimGuide.sh
```

**Windows** : The script was made using ```powershell```, so 
no additional dependencies.
## Screenshots
8051SimGuide.sh
![screenshot01](https://user-images.githubusercontent.com/44165144/201338550-e787a0f0-cc64-4e3b-acc3-c7c8e2afdfed.png)

## Authors

- [@rd](https://www.github.com/rd3ka)


