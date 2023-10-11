import socket
import json

serverHost = "192.168.1.127"
serverPort = 12005
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverHost, serverPort))

keep_communicating = True

while keep_communicating:
    operation = input("Enter one of the following operation: Add/Subtract/Random or close to end: ")
    if operation == "Close":
        keep_communicating = False
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        request = f"{operation} {num1} {num2}"

        Dictio = {"Operation": f"{operation}",
                "Number1": f"{num1}",
                "Number2": f"{num2}"}
        
        Json_file = json.dumps(Dictio)

        client.sendall(bytes(Json_file, encoding = "utf-8"))
        result = client.recv(1024).decode()
        print("Result is: ", result)
client.close()