import sqlite3
con = sqlite3.connect('example.db')
import socket as sck
dict = {}
s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
ACK = "logged"
s.bind(('0.0.0.0', 3000)) #solo su Server

while True:
    msg, add = s.recvfrom(4096)
    tmp = msg.decode().split(":")
    if (tmp[0].lower()=="nickname"):
        dict[tmp[1]]=add
        s.sendto(ACK.encode(),(add))
    else:
        tmp2 = msg.decode().split(",")
        rec = tmp2[1].split(":")
        s.sendto(tmp2[2].encode(),(dict[rec[1]]))
        print(f"mando '{tmp[2]}' a {rec[1]}")
    print(dict)

#f"sender:{nickname},receiver:{nickname_ricevente},msg"
s.close()