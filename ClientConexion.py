import socket

msgFromClient       = "Hola servidor UDP"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

##########################>>socket_family:#############################################
# Create a datagram socket
#es la familia de protocolos que es usada como mecanismo de transporte. 
#Estos valores son constantes tales como AF_INET, PF_INET, PF_UNIX, PF_X25, entre otras.
##########################>>socket_type:###############################################
#es el tipo de comunicación entre los dos extremos de la conexión, 
#usualmente se usa SOCK_STREAM TCP/IP para protocolos orientados a conexiones y SOCK_DGRAM UDP para protocolos sin conexiones.
#######################################################################################

#Creación del objeto tipo socket para el servidor
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
#Envia al servidor a traves del socket previamente creado por UDP
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Respuesta del servidor:{}".format(msgFromServer[0])

print(msg)