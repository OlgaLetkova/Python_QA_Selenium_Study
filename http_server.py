import socket
import datetime

end_of_stream = '\r\n\r\n'


def get_request_status(source_data):
    parameter = source_data.split("\r\n")[0].split(" ")[1]
    status = ""
    if "status=" in parameter:
        if parameter == "/?status=200" or parameter == "/?status="+"[^0-9]" or parameter == "/?status=":
            status = "200 OK"
        elif parameter == "/?status=201":
            status = "201 CREATED"
        elif parameter == "/?status=404":
            status = "404 NOT_FOUND"
        elif parameter == "/?status=503":
            status = "503 SERVICE_UNAVAILABLE"
        elif parameter == "/?a=1&status=500":
            status = "500 INTERNAL_SERVER_ERROR"
    else:
        status = "200 OK"

    http_response = (
        f"HTTP/1.0 {status}\r\n"
        f"Server: homeserver\r\n"
        f"Date: {datetime.datetime.now()}\r\n"
        f"Content-Type: text/html; charset=UTF-8\r\n"
        f"\r\n"
        )

    return http_response


def get_method(source_data):
    method = source_data.split()[0]
    return method


def get_source(source_data):
    source = source_data.split("\r\n")[1].split(" ")[1].replace(":", "\', ")
    return source


def get_response_status(source_data):
    parameter = source_data.split("\r\n")[0].split(" ")[1]
    status = ""
    if "status=" in parameter:
        if parameter == "/?status=200" or parameter == "/?status="+"[^0-9]" or parameter == "/?status=":
            status = "200 OK"
        elif parameter == "/?status=201":
            status = "201 CREATED"
        elif parameter == "/?status=404":
            status = "404 NOT_FOUND"
        elif parameter == "/?status=503":
            status = "503 SERVICE_UNAVAILABLE"
        elif parameter == "/?a=1&status=500":
            status = "500 INTERNAL_SERVER_ERROR"
    else:
        status = "200 OK"

    return status


def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        connection.send(get_request_status(client_data).encode()
                        + f"Request Method: {get_method(client_data)}\r\n".encode()
                        + f"Request Source: ('{get_source(client_data)})\r\n".encode()
                        + f"Response Status: {get_response_status(client_data)}\r\n".encode()
                        + f"{client_data}\r\n".encode())


with socket.socket() as serverSocket:
    serverSocket.bind(("127.0.0.1", 47296));
    serverSocket.listen();

    while (True):
        (clientConnection, clientAddress) = serverSocket.accept();
        handle_client(clientConnection)
        print(f"Connected to {clientAddress}");
