import sys
import socket

c_sock = socket.socket()
host = '192.168.56.111'
port = 8878

print("---Waiting for connection---")

try:
    c_sock.connect((host, port))
except socket.error as e:
    print(str(e))

msg = c_sock.recv(1024)
print(msg.decode('utf-8'))
c_msg = "Client connected!"
c_sock.send(c_msg.encode('utf-8'))

while True:

    print("\n------------------------------------------")
    print("\nMathematical Function")
    print("1 - Logarithmic Function (log)")
    print("2 - Square Root Function (sqrt)")
    print("3 - Exponential Function (exp)")
    print("4 - Tangent (tan)")
    print("5 - Sine (sin)")
    print("6 - Cosine (cos)")
    print("q - Quit")
    option = input('\nPlease choose any function: ')

    if option == '1':
        fx = "---Logarithmic Function (log)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == '2':
        fx = "---Square Root Function (sqrt)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == '3':
        fx = "---Exponential Function (exp)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == '4':
        fx = "---Tangent (tan)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == '5':
        fx = "---Sine (sin)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == '6':
        fx = "---Cosine (cos)---"
        print(fx)
        value = input("\nEnter a value: ")
        option = option + ":" + value
        c_sock.send(str.encode(option))

    elif option == 'q' or option == 'Q' or option == 'Quit' or option == 'quit':
        print("\n---Exiting system :)---\n")
        c_sock.send(str.encode(option))
        sys.exit()

    else:
        print("\nInput not recognize")
        sys.exit()

    msg = c_sock.recv(1024)
    print(msg.decode("utf-8"))

Csocket.close()
