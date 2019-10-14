import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hola Cliente UDP"
bytesToSend         = str.encode(msgFromServer)

##########################>>socket_family:#############################################
# Create a datagram socket
#es la familia de protocolos que es usada como mecanismo de transporte. 
#Estos valores son constantes tales como AF_INET, PF_INET, PF_UNIX, PF_X25, entre otras.
##########################>>socket_type:###############################################
#es el tipo de comunicación entre los dos extremos de la conexión, 
#usualmente se usa SOCK_STREAM TCP/IP para protocolos orientados a conexiones y SOCK_DGRAM UDP para protocolos sin conexiones.
#######################################################################################

#Creación del objeto tipo socket para el servidor
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
#Se indica que puerto se va a mantener en escucha en el servidor y el host
#Este método vincula una dirección (hostname, número de puerto) a un socket.
UDPServerSocket.bind((localIP, localPort))

print("El servidor esta en linea y en escucha")

# Listen for incoming datagrams

while(True):

	#a través del método recvfrom() se recibe información
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Mensaje del cliente:{}".format(message)
    clientIP  = "Dirección IP del cliente:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    #a través de este método se envia información
    UDPServerSocket.sendto(bytesToSend, address)