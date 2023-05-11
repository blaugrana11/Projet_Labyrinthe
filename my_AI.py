import socket
import json
import sys

Playing = True
# Configuration
HOST = "localhost"
PORT = int(sys.argv[1])
NAME = "Nabil et Mohamed"
MATRICULES = ["21168", "20130"]
SERVER_ADRESS = ('',3000)

# Inscription
subscribe_msg = {
        "request": "subscribe",
        "port": PORT,
        "name": NAME,
        "matricules": MATRICULES
    }
 # Établissement de la connexion en créant la socket et en envoyant la requête d'inscription au serveur".
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.settimeout(5)
    try:
        server_socket.connect(SERVER_ADRESS)
        server_socket.sendall(json.dumps(subscribe_msg).encode())
        response = json.loads(server_socket.recv(4096).decode())
        print(response)
    except socket.timeout:
        print("Connexion au serveur échouée")
        pass

 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.listen()

    while Playing:
        s.settimeout(5)
        try: 
            # Acceptation de la connexion entrante
            client_socket, client_address = s.accept()
            with client_socket:
                print('Connexion de', client_address)

                # Réception du message envoyé par le serveur
                data = client_socket.recv(16000).decode()
                print('Reçu', repr(data))

                # Analyse du message reçu et envoi de la réponse appropriée
                message = json.loads(data)
                if message['request'] == 'ping':
                    response = {"response": "pong"}
                    print(response)
                    client_socket.sendall(json.dumps(response).encode())
                '''elif message['request'] == 'play':
                    reponse()'''
                
                #print(message['state'])

        except socket.timeout:
            pass