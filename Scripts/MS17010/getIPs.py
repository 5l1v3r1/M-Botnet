import subprocess
import os

powershellfilename = "1.ps1"

def execute_command(command):
    if len(command) > 0:
        print(command)
        result = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
        out, err = result.communicate()
        return out

def getMYIP():
    ips=[]
    out = execute_command("ipconfig").split("\r\n")
    for line in out:
        if "  IPv4 Address" in line:
            line = line.split(":")[1]
            #print(line)
            ips.append(line)
    return ips


def GetAllPossibleIPs1(ips):
    ips2 = []
    for ip in ips:
        ip = ip.split(".")[:-1]
        ips2.append(ip)
    return ips2

def GetAllPossibleIPs2(ips):
    #[' 192', '168', '1']
    all =[]
    for ip in ips:
        for i in range(1,255):
            ip.append(str(i))
            s = '.'.join(ip)
            newIP = str(s)
            all.append(newIP)
            ip.pop()
    return all


def save(all):
    filee = open("IPList.txt","w+")
    for addr in all:
        addr = addr.strip(" ")
        filee.write(addr+"\n")
    filee.close()

def main():
    ips = getMYIP()
    ips2 = GetAllPossibleIPs1(ips)
    all = GetAllPossibleIPs2(ips2)
    save(all)
    os.system("Powershell -ExecutionPolicy ByPass -File "+powershellfilename)
    print("Print")

main()
