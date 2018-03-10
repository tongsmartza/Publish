from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)     # Server socket address 
s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket
s.connect(addr)

topic = ''
data = ''


while(1):
    command = input('Insert your command <topic/publish/cancel> : ')
    commander , line = command.split(" ")

    

    if(commander == 'cancel' and line == topic):
        print('\t\n' +topic+' is Cancel \n')
        topic = ''
        data = ''
        txtout = 'pub,'+topic+','+data+','+commander
        print(txtout)
        s.sendto(txtout.encode('utf-8'), addr)
    elif(commander == 'cancel' and line != topic):
        print('Topic Invalid')

    else:
       if(commander == 'topic'):
           topic = line # text for prompt
           print(topic)
       if(commander == 'publish'):
        #sys.stdout.flush()
        #txtout =  sys.stdin.readline().strip() # Take input from user keyboard
           data = line
           print(topic+' > '+data)
           txtout = 'pub,'+topic+','+data+','+commander
           print(txtout)
           s.sendto(txtout.encode('utf-8'), addr) # Convert to byte type and send


    #while(1):
        #print('%s> ' %(topic), end='') # Print the prompt
        
        #modifiedMsg, srvAddr = s.recvfrom(2048) # Wait for modified text from the server
        #print (modifiedMsg.decode('utf-8'))     # Print the modified text.
s.close()