
import threading

FORMAT          = 'UTF-8'
DISCONNECT_MSG  = "DISC"
CONNECTED       = True
HEADER          = 1024

''' ========================================================================== '''

''' Server Functions '''

def handle_client( client, addr ) :
    
    global FORMAT        
    global DISCONNECT_MSG
    global CONNECTED     
    global HEADER        

    print( f"The client address is: {addr}" )

    while CONNECTED == True :
        
        client_msg = client.recv( HEADER )
        
        client_msg_decoded = client_msg.decode(FORMAT)
        
        print( f"{addr} is sending you this message: {client_msg_decoded}" )

        if client_msg_decoded == DISCONNECT_MSG :
            
            print('========================================================================')
            print( f"{addr} is disconnecting from the Server......." )
            
            client.close()
                
            CONNECTED = False
            
        elif (client_msg_decoded != None) and (client_msg_decoded != DISCONNECT_MSG) :
    
            print('========================================================================')
            
            server_msg = str( input( "Please enter the message you want to send to the client: " ) )
        
            server_msg_encode = server_msg.encode( FORMAT )
            
            client.send( server_msg_encode )
  
def server_start( server, clients_nums ) :
    
    server.listen( clients_nums )

    print( f"[LISTENING] Server is listening on {server}" )

    while True:
        
        # Waiting till the client connect:
        client, address = server.accept() 
    
        thread = threading.Thread( target = handle_client, args = ( client, address ) )
    
        thread.start()
        
        print( f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}" )
        
''' ========================================================================== '''

''' Client Functions '''

def client_send( client ) :
    
    global FORMAT        
    global DISCONNECT_MSG
    global HEADER        

    print('==========================================================')
    
    msg = str( input( "please, enter the message that you want to send: " ) )
    
    msg_encoded = msg.encode( FORMAT )
    
    client.send( msg_encoded )

def client_receive( client ) :
    
    global FORMAT        
    global DISCONNECT_MSG
    global HEADER        
    
    print('==========================================================')
    
    recv_msg = client.recv( HEADER )
    
    recv_msg_decoded = recv_msg.decode(FORMAT)
    
    print( f"The server is sending to you this message: {recv_msg_decoded} " )
    
    if recv_msg_decoded == DISCONNECT_MSG :
        
        print('========================================================================')
        print( "You are now disconnecting from the Server......." )
            
        client.close()


''' ========================================================================== '''




