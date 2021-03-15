import socket

sysIP = "192.168.1.1"
sysPORT = 514
sysBUFFER = 1024
sysFilter = "touch"

sysSOCKET = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sysSOCKET.bind((sysIP,sysPORT))
print("Syslog Server has started")
while 1==1:
    recData, recAdd = sysSOCKET.recvfrom(sysBUFFER)
    stringRecieved = recData.decode('utf-8')
    if sysFilter in stringRecieved:
        sourceIP = recAdd[0]
        splitCommand = stringRecieved.split(" ", 1)
        the_file = open(splitCommand[1],"w")
        sysSOCKET.close()
        secondSocket = ocket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        secondSocket.bind((sysIP,sysPORT))
        while 1==1:
            recDataTwo, recAddTwo = secondSocket.recvfrom(sysBUFFER)
            secondSourceIP = recAddTwo[0]
            if sourceIP == secondSourceIP:
                 the_file.write(recDataTwo.decode('utf-8'))
            else:
                break
        secondSocket.close()

sysSOCKET.close()
