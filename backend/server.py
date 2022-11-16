import socket

 # A TCP based echo server
echoSocket = socket.socket();

# Bind the IP address and the port number
echoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
echoSocket.bind(("0.0.0.0", 8080));

# Listen for incoming connections
echoSocket.listen();



# Handle one request from client
while(True):
    # Start accepting client connections
        (conn, address) = echoSocket.accept();

        data = conn.recv(1024).decode()
        if not data: break
        print(f"recived {data} from {address}");
        #TO DO: replace whith sent file http://michaldul.com/python/sendfile/
        file_scores = open("scores.txt", "r")
        response = f'HTTP/1.0 200 OK\n\n {file_scores.read()}' 
        file_scores.close()

        # Send back what you received
        conn.sendall(response.encode());
        conn.close
echoSocket.close()