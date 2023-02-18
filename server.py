import os
import socket

from sock_mod import *     

if __name__ == '__main__' :

    os.system('cls')

    print()
    # Write your code here:
     
    # Select: IPv4, TCP: 
    myServer = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
    
    PORT = 5050

    # Get the IP of the device:
    SERVER_IPv4 = socket.gethostbyname( socket.gethostname() )
    
    SERVER_ADDR = ( SERVER_IPv4, PORT )
    
    myServer.bind( SERVER_ADDR )  
    
    server_start( myServer, 1 )
    
    # The end of your code. 

