import socket, threading

class TreadForClient(threading.Thread):
    """
    Création d'un thread pour pour un client.
    Permet de recevoir les messages du client associé et l'envoyer au autre client
    """
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion
        self.connexionTest()


    def run(self):
        """
        Boucle principale, reçoit les messages et les envoies au autre clients connectés au serveur
        """
        try:  # fonctionne avec le except
            self.getPseudo()
            while True:
                data = self.connexion.recv(1024).decode("utf8")
                msg = self.pseudo + '> ' + data
                print(msg)
                self.sendAll(msg)

        except ConnectionResetError:  # Si l'utilisateur se déconnecte
            self.deconnexion()

    def getPseudo(self):
        """
        Attend la reception du pseudo.
        Fonction bloquante !!!
        """
        self.pseudo = self.connexion.recv(1024).decode("utf8")

    def deconnexion(self):
        """
        Gestion de la deconnexion du client
        """
        connexion_list.remove(self.connexion)
        self.connexion.close()

    def sendAll(self, msg):
        """
        Envoie le message reçu à tout les utilisateurs sauf celui qui l'a envoyé
        """
        for conn in connexion_list:
            if conn != self.connexion:
                conn.send(msg.encode("Utf8"))

    def connexionTest(self):
        """
        Permet de tester la connexion
        """
        connexion.send('OK'.encode("Utf8"))


host, port = '', 80

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création du serveur en TCP
socket.bind((host, port))
print('Le serveur est prêt')

connexion_list = []  # Permet d'ajouter toute les connexions pour envoyer les messages

while True:
    try :
        socket.listen(5)
        connexion, address = socket.accept()
        print('Connexion de :', address)
        connexion_list.append(connexion)

        my_thread = TreadForClient(connexion)  # Création du theard pour le client
        my_thread.start()
    except:
        break


socket.close()
