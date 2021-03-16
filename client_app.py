import socket

from api.message import receive_int, send_str, receive_str

from client_io.main_menu import main_menu

HOST = socket.gethostname()
GATE = 19999
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket_client.connect((HOST, GATE))
    option = main_menu()
    if option == 2:
        socket_client.send(option.to_bytes(4, byteorder="little", signed=True))
        pid_length = receive_int(socket_client)
        print('receiving "'+str(pid_length)+'" messages from server...')

        for i in range(pid_length):
            msg = receive_str(socket_client)
            print(msg)
        socket_client.close()

except Exception as error:
    print(str(error))
