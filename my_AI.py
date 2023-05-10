import socket
import json
import time
import sys
from typing import Optional, List, Tuple
from collections import deque


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


def neighbors(state, maze):
    x, y = state
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:  # 1 est supposé représenter un mur
            result.append((nx, ny))

    return result


def bfs(state, goal):
    frontier = deque()  # Une file d'attente pour les états à explorer
    frontier.append(state)  # On commence par l'état initial
    came_from = {}  # Un dictionnaire qui associe à chaque état l'état précédent
    came_from[state] = None  # L'état initial n'a pas d'état précédent

    while len(frontier) > 0:  # Tant qu'il reste des états à explorer
        current = frontier.popleft()  # On prend le premier état de la file d'attente

        # Si l'état courant est l'état final, on a terminé
        if current == goal:
            break

        # Sinon, pour chaque voisin de l'état courant
        for next in neighbors(current):
            # Si on n'a pas encore exploré ce voisin
            if next not in came_from:
                frontier.append(next)  # On l'ajoute à la file d'attente pour l'explorer plus tard
                came_from[next] = current  # On note qu'on peut atteindre ce voisin à partir de l'état courant

    # Une fois que l'on a atteint l'état final, on peut retrouver le chemin qui y mène en remontant les états précédents
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()  # On inverse le chemin pour qu'il commence par l'état initial
    return path  # Et on le renvoie

# Établissement de la connexion en créant la socket et en envoyant la requête d'inscription au serveur".
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

                elif message['request'] == 'play':
                    maze = message["state"]['board']  # Le labyrinthe est supposé être envoyé dans chaque message 'play'
                    ind_player = message["state"]["current"]
                    player_position = message['state']["positions"][ind_player]  # La position du joueur
                    print(player_position)
                    goal_position = message["state"]['target']  # La position du but

                    path = bfs(player_position, goal_position, maze)  # On trouve un chemin vers le but

                    if path:
                        next_position = path[1]  # On prend le deuxième élément du chemin, car le premier est la position actuelle du joueur
                        dx, dy = next_position[0] - player_position[0], next_position[1] - player_position[1]

                        # On déduit la direction à partir de la différence de positions
                        if dx == 0 and dy == 1:
                            direction = "right"
                        elif dx == 0 and dy == -1:
                            direction = "left"
                        elif dx == 1 and dy == 0:
                            direction = "down"
                        elif dx == -1 and dy == 0:
                            direction = "up"

                        response = {"response": direction}
                    client_socket.sendall(json.dumps(response).encode())


                

        except socket.timeout:
            pass