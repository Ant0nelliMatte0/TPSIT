import socket as sck
import threading

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

def rec():
    while True:
        RecMsg, add = s.recvfrom(4096)
        print(RecMsg.decode())

def send(add):
    while True:
        receiver = input("insert the nickname of the receiver:\n ")
        text= input(":\n ")
        msg = f"{nickname},{receiver},{text}"
        s.sendto(msg.encode(),add)
    s.close()

nickname = input("nickname: ")
msg = f"nickname:{nickname}"
s.sendto(msg.encode(),('192.168.0.117',3000))
ack,add =s.recvfrom(4096)
print(ack.decode(

sndr = threading.Thread(target=send, args=(add,))
rcvr = threading.Thread(target=rec)

sndr.start()
rcvr.start()

#f"sender:{nickname},receiver:{nickname_ricevente},msg"