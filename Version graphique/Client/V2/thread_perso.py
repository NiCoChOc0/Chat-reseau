import threading, socket

class ThreadForRead(threading.Thread):
    """
    Création d'un thread que permet de lire les messages reçu par le serveur
    """
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        """
        Boucle principale
        """
        while True:
            try:
                msgServeur = self.socket.recv(1024).decode("Utf8")
                print(msgServeur) # Changer pour qu'on puisse l'afficher sur notre fenêtre !

            except ConnectionResetError:  # si le serveur plante, la connexion se ferme
                self.socket.close()
                break


class ThreadForWrite(threading.Thread):
    """
    Création d'un thread que permet d'envoyer des messages au serveur
    """
    def __init__(self, socket, pseudo):
        threading.Thread.__init__(self)
        self.socket = socket
        self.socket.send(pseudo.encode("Utf8"))

    def run(self):
        """
        Boucle principale
        """
        while True:
            try:
                msg = input() # Prendre le message de la zone de texte !
                print("moi> " + msg)  # Afficher dans la partie graphique !
                self.socket.send(msg.encode("Utf8"))
            except:  # si le serveur plante, la connexion se ferme
                self.socket.close()
                break