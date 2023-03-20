import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = ('localhost', 4000)

try :
    s.connect((host, port))
    print("Le client se connecte... ")
    s.listen()
    data = ' J peux moi aussi ouuuu que les petits ? T as les kramptés ? Hein ? Inpainyain, Quoicoubeh, quoicoubeh, quoicoubeh 🎶 '
    data = data.encode("utf8")
    s.sendall(data)
except ConnectionRefusedError :
    print(" Connexion au serveur échouée ")

finally :
    s.close()


