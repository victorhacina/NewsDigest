import socket
import os

INTERFACE = "0.0.0.0"
PORT = 8080

FNAME = "result.txt"


 # A TCP based echo server
echoSocket = socket.socket()

# Bind the IP address and the port number
echoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
echoSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
echoSocket.bind((INTERFACE, PORT))

# Listen for incoming connections
echoSocket.listen()

print("\n=== SERVER LISTENING ===\n")
print(f"{ INTERFACE } : { PORT } \n\n\n ")

# Handle one request from client
while(True):
    # Start accepting client connections
        (conn, address) = echoSocket.accept()

        data = conn.recv(1024).decode()
        if not data: break

        print(f"Connection from {address} \n")
        print(data)

        file_scores = open(FNAME, "rb")
        file_scores_stats = os.stat(FNAME)
    

    
        conn.send(b'HTTP/1.1 200 OK \n')
        conn.send(f'Content-Length: { file_scores_stats.st_size } \n'.encode())
        conn.send(b'Content-Type: text/json; encoding=utf8 \n')
        conn.send(b'Access-Control-Allow-Origin: * \n')
        conn.send(b'Connection: close \n')
        conn.send(b'\n')
        conn.sendfile(file_scores)
        

        file_scores.close()
        conn.close
        
echoSocket.close()