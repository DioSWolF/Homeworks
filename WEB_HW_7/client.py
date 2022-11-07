from time import sleep
import socket

host = 'localhost'
port = 8080

def simple_client(host, port):
    while True:
        cleint_data = client_start(host, port)
        if not cleint_data: 
            break   
        data = listen_client(host, port)
        if not data: 
            break   

    print("closed")


def listen_client(host, port):
    with socket.socket() as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        new_sock, address = sock.accept()
        print(new_sock)
        print(address)
        data = new_sock.recv(1024)
        print(f"Message: {data}")
        new_sock.send(b"OK")

    return data

def client_start(host, port):

    with socket.socket() as sock:
        try:
            sock.connect((host, port))
            while True:
                user_input = input("Write text: ")
                sock.sendall(user_input.encode())
                data = sock.recv(1024)

                print(f'From server: {data}')

                if data == b"OK" or data == b"exit": 
                    return data 
                
        except ConnectionRefusedError:
            sleep(0.5)


if __name__ == '__main__':
    simple_client(host, port)
