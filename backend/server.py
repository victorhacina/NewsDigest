import socket
import os

INTERFACE = "0.0.0.0"
PORT = 8080

FNAME = "/home/myuser/NewsDigest/backend/result.txt"


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
        conn.settimeout(2)

        try:

            data = conn.recv(1024).decode()
            if not data: continue

            print(f"Connection from {address} \n")
            print(f'{data} \r\n')


            http_method = data.splitlines()[0].split(" ")[0]
            http_location = data.splitlines()[0].split(" ")[1]

            if http_method != "GET" or http_location != "/" : 
                conn.send(b'HTTP/1.1 404 \r\n')
                conn.send(b'Connection: close \r\n')
                conn.close
                continue





            file_scores_stats = os.stat(FNAME)
        
            conn.send(b'HTTP/1.1 200 OK \r\n')
            conn.send(f'Content-Length: { file_scores_stats.st_size } \r\n'.encode())
            conn.send(b'Content-Type: text/json; encoding=utf8 \r\n')
            conn.send(b'Access-Control-Allow-Origin: * \r\n')
            conn.send(b'Connection: keep-alive \r\n')
            conn.send(b'\r\n')

            with open(FNAME, "rb") as f:
                conn.sendfile(f)
            conn.send(b'\r\n')
            conn.close

        except socket.timeout as e:
            print(f"Timeout: {e}")
            continue

        except Exception as e:
            print(f"Exception: {e}")
            continue
        
echoSocket.close()