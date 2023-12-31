import socket
import threading

class TreadForClient(threading.Thread):
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion
        connexion.send('OK'.encode("Utf8")) # Vérification de connexion
        self.pseudo = self.connexion.recv(1024).decode("utf8") # Reception du pseudo


    def run(self):
        while True:
            data = self.connexion.recv(1024).decode("utf8")
            msg = self.pseudo +'> '+ data
            print(msg)
            self.hystoric.append(msg)
            self.hystoric.pop(0)
            """
                Condition de sortie (quand l'utilisateur se déconnecte)
            """
            for conn in connexion_list:
                conn.send(msg.encode("Utf8")) # Envoie au autre client



host, port = '', 80

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du serveur en TCP
socket.bind((host, port))
print('Le serveur est prêt')

connexion_list = [] # Permet d'ajouter toute les connexions pour envoyer les messages

while True:
    socket.listen()
    connexion, address = socket.accept()
    print('Connexion de :', address)
    connexion_list.append(connexion)

    my_thread = TreadForClient(connexion) # Création du theard pour le client
    my_thread.start()


connexion.close()
socket.close()
