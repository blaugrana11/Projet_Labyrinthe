import json
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = ('localhost', 4000)
request = {
   "request": "subscribe",
   "port": 8888,
   "name": "fun_name_for_the_client",
   "matricules": ["12345", "67890"]
}

request_ping = {
   "response": "pong"
}

request_coup = {
   "response": "move",
   "move": the_move_played,
   "message": "Fun message"
}

surrender = {
   "response": "giveup",
}

try :
    s.connect((host, port))
    print("Le client se connecte... ")
    s.sendall(json.dumps(request).encode())
    response = s.recv(2048).decode()
    print(response)
except ConnectionRefusedError :
    print(" Connexion au serveur échouée ")

finally :
    s.close()

# Création de la socket et écoute sur le port de souscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 8888))
    s.listen()

    while Variable:
        s.settimeout(5)
            
        try: 
            # Acceptation de la connexion entrante
            client_socket, client_address = s.accept()
            print('Connexion de', client_address)

            # Réception du message envoyé par le serveur
            data = client_socket.recv(1024).decode()
            print('Reçu', repr(data))

            # Analyse du message reçu et envoi de la réponse appropriée
            message = json.loads(data)
            if message['request'] == 'ping':
                response = {"response": "pong"}
                print(response)
                client_socket.sendall(json.dumps(response).encode())

            # Fermeture de la connexion
            client_socket.close()
        except:
            print("Trop long pour l'accept")
            pass

        Variable = False #Pour arrêter la boucle étant donné qu'on est déja accepé