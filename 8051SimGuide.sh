#!/bin/bash

RT_DOWN="https://cdn.azul.com/zulu/bin/zulu17.38.21-ca-jre17.0.5-linux_x64.tar.gz"
SIM_DOWN="http://www.edsim51.com/8051simulator/edsim51di.zip"

function ic() {
    ping -c 2 1.1.1.1 > /dev/null 2>&1  && echo "Internet Connectivity Available" || exit 1
}

function greetings() {
    echo "";    
    echo " █████╗  ██████╗ ███████╗ ██╗███████╗██╗███╗   ███╗ ██████╗ ██╗   ██╗██╗██████╗ ███████╗";
    echo "██╔══██╗██╔═████╗██╔════╝███║██╔════╝██║████╗ ████║██╔════╝ ██║   ██║██║██╔══██╗██╔════╝";
    echo "╚█████╔╝██║██╔██║███████╗╚██║███████╗██║██╔████╔██║██║  ███╗██║   ██║██║██║  ██║█████╗  ";
    echo "██╔══██╗████╔╝██║╚════██║ ██║╚════██║██║██║╚██╔╝██║██║   ██║██║   ██║██║██║  ██║██╔══╝  ";
    echo "╚█████╔╝╚██████╔╝███████║ ██║███████║██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║██████╔╝███████╗";
    echo " ╚════╝  ╚═════╝ ╚══════╝ ╚═╝╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝╚═════╝ ╚══════╝";
    echo "                                                                                        ";
    echo "This script automates the download and installation of edsim51di";
    echo ""

    read -p "Hit ENTER to continue";
    echo ""
}

function p1() {
    local fname=zulu17.38.21-ca-jre17.0.5-linux_x64.tar.gz 
    java --version > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        find ./.data -name JRE > /dev/null 2>&1 
        if [ $? -ne 0 ]; then
            ic
            echo "Getting JavaRunTime Ready!"
            curl --progress-bar $RT_DOWN -o "$fname" | tee /dev/null
            tar xf $fname && rm $fname 
            mv zulu17.38.21-ca-jre17.0.5-linux_x64 JRE
        else 
            echo "JavaRunTime already downloaded, skipping"
            retVal=0
        fi
    else 
        echo "JavaRunTime already in PATH, skipping"
        retVal=1
    fi
    return $retVal
}

function p2() {
    find ./.data -name edsim51di > /dev/null 2>&1  
    if [ $? -eq 0 ]; then
        retV=0
    else
        ic
        echo "Setting up edsim51di"
        curl --progress-bar $SIM_DOWN -o "edsim51di.zip" | tee /dev/null
        unzip edsim51di.zip && rm edsim51di.zip
        retV=0
    fi
    return $retV
}

function execute() { 
    if [ $1 -eq 0 ]; then
        ./.data/JRE/bin/java -jar .data/edsim51di/edsim51di.jar 
    else
        java -jar edsim51/edsim51di.jar
    fi
}

function main() {
    clear
    greetings
    p1 
    retp1=$?
    p2
    retp2=$?

    if [ -d ".data" ]; then
        [ $retp2 -eq 0 ] && execute $retp1 || exit 0 
    else 
        mkdir .data && mv JRE edsim51di .data 
        [ $retp2 -eq 0 ] && execute $retp1 || exit 0 
    fi
    rm -rf *.ser
}

main
