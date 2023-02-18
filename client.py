
import socket

from sock_mod import *  

if __name__ == '__main__' :

    print()
    # Write your code here:
     
    SERVER_IPv4     = '192.168.1.5'
    PORT            = 5050
    SERVER_ADDR     = ( SERVER_IPv4, PORT )
    
    # Select: IPv4, TCP: 
    yourClient = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
    
    yourClient.connect( SERVER_ADDR )

    client_send( yourClient )

    client_receive( yourClient )

    client_send( yourClient )

    # The end of your code. 
    print(), print()









