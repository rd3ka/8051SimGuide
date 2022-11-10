#!/bin/bash

RT_DOWN="https://cdn.azul.com/zulu/bin/zulu17.38.21-ca-jre17.0.5-linux_x64.tar.gz"
SIM_DOWN="http://www.edsim51.com/8051simulator/edsim51di.zip"

function ic() {
    ping -c 2 1.1.1.1 > dev/null 2>&1  && echo "Internet Connectivity Available" || exit 1
}

function p1() {
    local fname=zulu17.38.21-ca-jre17.0.5-linux_x64.tar.gz 
    java --version > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        find ./.data -name JRE > /dev/null 2>&1 
        if [ $? -ne 0 ]; then
            ic
            curl $RT_DOWN -o "$fname"
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
        curl $SIM_DOWN -o "edsim51di.zip"
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
    p1 
    retp1=$?
    p2
    retp2=$?

    if [ -d ".data" ]; then
        [ $retp2 -eq 0 ] && execute $retp1 || exit 0 
        rm -rf $(ls -I run.sh)
    else 
        mkdir .data && mv $(ls -I run.sh) .data 
        [ $retp2 -eq 0 ] && execute $retp1 || exit 0 
    fi
}

main
