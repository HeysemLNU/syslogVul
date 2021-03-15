import socket

sysIP = "192.168.1.1"
sysPORT = 514
sysBUFFER = 1024
sysFilter = "touch"

sysSOCKET = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sysSOCKET.bind((sysIP,sysPORT))

while 1==1:
    recData, recAdd = sysSOCKET.recvfrom(sysBUFFER)
    print("message: ", recData)
    stringRecieved = recData
    if sysFilter in stringRecieved
        print("Recieved")

sysSOCKET.close()
