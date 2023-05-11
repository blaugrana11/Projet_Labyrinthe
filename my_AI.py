import socket
import json
import sys

Playing = True

def play() :  #Fonction basique qui renvoie une nouvelle position la ou c est possible de maniere aleatoire
    ind_player = message['state']['current']
    pos = message['state']['positions'][ind_player]
    print(pos)
    right = 1
    left = -1
    up = -7
    down = 7
    for key, value in message['state']['board'][pos].items() :
        if value == True :
            if key == 'S':
                new_pos = pos + down
            elif key == 'N':
                new_pos = pos+up
            elif key == 'E':
                new_pos = pos + right
            elif key == 'W':
                new_pos = pos + left
    
    move = {'tile' : message['state']['tile'], "gate": "B", "new_position": new_pos}
    client_resp = {
   "response": "move",
   "move": move,
   "message": "Yo !"
    }
    client_socket.sendall(json.dumps(client_resp).encode())


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
                elif message['request'] == 'play':
                    play()
                

        except socket.timeout:
            pass