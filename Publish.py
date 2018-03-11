# Group Network need some Carry
#       58070501006 Karntawan   Udomluksopin
#       58070501046 Peerakit    Boonkittiporn
#       58070501054 Methawat    Thanapairin
#       58070501069 Sirapong    Phoosawan
 
from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)     # Server socket address 
s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket
s.connect(addr) #Socket Connected to Server

topic = ''  #set topic is null
data = ''   #set data is null
print ('----- Publisher is started -----')
while(1):
    command = input('Insert your command <topic/publish/cancel> : ')
    commander , line = command.split(" ")   #split command input and keep command to commander, keep data in line

    if(commander == 'cancel' and line == topic):    #check command is cancel and topic is same 
        print('\tTopic ' +topic+' is Cancel \n')    #print topic is cancel
        topic = ''  #reset topic is null
        data = ''   #reset data is null
        txtout = 'pub,'+topic+','+data+','+commander    #Pattern data for send to server
        s.sendto(txtout.encode('utf-8'), addr)  #Convert to byte type and send to server

    elif(commander == 'cancel' and line != topic):  #check command is cancel but topic is not same
        print('\tTopic Invalid Input \n')   #show message invalid input topic

    else:
       if(commander == 'topic'):    
           topic = line     #set topic is line variable
           print('\tTopic is > '+topic+'\n') #print topic
       if(commander == 'publish'):
           data = line  #set data is line variable
           print('\t'+topic+' > '+data+'\n') # print data
           txtout = 'pub,'+topic+','+data+','+commander #Pattern data for send to server
           s.sendto(txtout.encode('utf-8'), addr) #Convert to byte type and send to server

s.close()