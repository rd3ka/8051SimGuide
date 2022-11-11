Import-Module BitsTransfer

$runtime='https://cdn.azul.com/zulu/bin/zulu17.38.21-ca-jre17.0.5-win_x64.tar.gz'
$sim='http://www.edsim51.com/8051simulator/edsim51di.zip'

function connection() {
    $t = Test-Connection 1.1.1.1 -Quiet
    return $t
}

function find($command) { 
    $r=(Get-ChildItem -Recurse | Where {$_.Name -eq $command} | Select BaseName)
    if ($r -ne $null) {
        $r = $r.BaseName.Contains($command)
    }
    else { 
        $r = $false
    }
    return $r
}

function Test-CommandExists($command) {
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = ‘stop’
    try {
        if (Get-Command $command) {
            “$command exists”
         }
    }
    Catch {
        “$command does not exist”
    }
    Finally {
        $ErrorActionPreference=$oldPreference
    }
} 

function p1() {
    $fname = 'zulu17.38.21-ca-jre17.0.5-win_x64'
    $check = Test-CommandExists 'java --version'

    if ( $check.Contains('not') ) {
        
        $fc = find 'bin'   

        if (!$fc) {
            $filename = $fname + '.tar.gz'
            Start-BitsTransfer -Source $runtime -Destination $filename
            tar.exe xf $filename; rm $filename
            
            $src = $PWD.Path + '\' + $fname
            Rename-Item $src JRE

            $src = $PWD.Path + '\' + 'JRE'
            Move-Item $src data
        }
        else {
            echo "JavaRunTime already downloaded, skipping"
        }
    }
    
    else {
        echo "JavaRunTime already in PATH, skipping"
    }    
}

function p2() {
    $fname = 'edsim51di'
    $f = find $fname
    if ($f) {
        echo "edSim51di already downloaded, skipping"
    }
    else {
        $filename = $fname + '.zip'
        Start-BitsTransfer -Source $sim -Destination $filename
        Expand-Archive -Force $filename; rm $filename

        $src = $PWD.Path + '\' + $fname
        Move-Item $src data

    }
}

function execute($val) {
    if ($val -eq 0) {
        .\data\JRE\bin\java -jar .\data\edsim51di\edsim51di\edsim51di.jar
    }
    else {
        java -jar .\data\edsim51di\edsim51di\edsim51di.jar
    }
}

function terminateExp() {
    $a = (New-Object -comObject Shell.Application).Windows() | ? { $_.FullName -ne $null} | ? { $_.FullName.toLower().Endswith('\explorer.exe') }
    $a | % {  $_.Quit() }
}

function main() {
    terminateExp
    $e = connection
   
    if (!$e) {
        echo 'Please connect to the Internet and try again'
        exit
    }
     
    $d = find 'data'
    if ( !$d ) {
        mkdir data | Out-Null
        p1
        p2
        execute 0

    }
    else {
        p1
        p2
        execute 0
    }
    rm -Recurse *.ser
}

main