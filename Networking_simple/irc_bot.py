import socket
import sys
import random
 
class IRC:
 
    irc = socket.socket()  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " :" + msg + "\n").encode())

    def connect(self, server, channel, botnick):
        #defines the socket
        print ("connecting to: "+server)
        self.irc.connect((server, 6667))
        self.irc.send(("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!\n").encode()) #user authentication
        self.irc.send(("NICK " + botnick + "\n").encode())
        self.irc.send(("JOIN " + channel + "\n").encode())
 
    def get_text(self):
        text=self.irc.recv(2040)
        return text

channel = "#tchan123"
server = "irc.freenode.net"
nickname = "tbotty0"
 
irc = IRC()
irc.connect(server, channel, nickname) 
 
while 1:
    text = irc.get_text()
    print (text.decode())

    if b"PRIVMSG" in text and channel.encode() in text and b":hello" in text:
        user = text.strip().split(b"~")[0][1: -1].decode()
        irc.send(channel, "Hello " + user + "!\n")