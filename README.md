# 8051SimGuide v2

## UPDATE: November, 2022

At the time of writing the script, I was still a student and was trying out different things to work on, so that I could improve on my programming skills. Hence, after 2 years of the original script. I've learnt a lot and gathered a lot programming experience, as when compared to the time of writting this script. This has led me to use shell scripting using [bash shell](https://www.gnu.org/software/bash/) to redo my original script which in turn optimizes the code count and also the performance without any overhead dependencies.

# Installation & Dependencies

**Linux** : The script was made to run in bash shell which is the default shell is most modern distributions.
 ``` curl``` , ```tee```, ```ping```, ```zip``` and ```tar```
command line programms are used. These command line programs come preinstalled and are essential part of the kernel in most 
distributions.

In case, the script errors out, please installed them manually in accordance to your distro:

```
  Debain/Ubuntu : sudo apt-get install curl, tee, ping, tar
  Arch          : sudo pacman -S curl, tee, ping, tar
  Fedora/RedHat : sudo dnf install curl, tee, ping, tar
```
Before running the script don't forget to change the execution group/policy
```
  chmod +x 8051SimGuide.sh
```

**Windows** : The script was made using ```powershell 5```, so 
no additional dependencies are required to be met.

# Screenshots
[8051SimGuide.sh](https://github.com/rd3ka/8051SimGuide/blob/v2/8051SimGuide.sh)

![screenshot_02](https://user-images.githubusercontent.com/44165144/201364637-f5a0e490-366d-471d-92b1-2779d96aad4f.png)

NOTE: [8051SimGuide.ps1](https://github.com/rd3ka/8051SimGuide/blob/v2/8051SimGuide.ps1) does not have any Command Line Interface or GUIs