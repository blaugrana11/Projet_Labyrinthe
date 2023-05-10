import socket
import json
import time
import sys
from typing import Optional, List, Tuple

server_address = ('', 3000)
Playing = True

port = int(sys.argv[1])

# Création de la requête d'inscription
request = {
    "request": "subscribe",
    "port": port,
    "name": "Nabil et Mohamed",
    "matricules": ["21168", "20130"]
}

# Établissement de la connexion en créant la socket et en envoyant la requête d'inscription' au serveur".
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    try:
        s.connect(server_address)
        s.sendall(json.dumps(request).encode())
        response = s.recv(2048).decode()
        print(response)
    except socket.timeout:
        print("Connexion au serveur échouée")
        pass

# Création de la socket et écoute sur le port d'inscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', port))
    s.listen()

    while Playing:
        s.settimeout(5)
            
        try: 
            # Réception et acceptation de la connexion entrante
            client_socket, client_address = s.accept()
            with client_socket:
                print('Connexion de', client_address)

                # Réception du message envoyé par le serveur
                data = client_socket.recv(16000).decode()
                print('Reçu', repr(data))

                # Traitement du message et envoi de la réponse adéquate
                message = json.loads(data)
                if message['request'] == 'ping':
                    response = {"response": "pong"}
                    print(response)
                    client_socket.sendall(json.dumps(response).encode())
        except socket.timeout:
            pass