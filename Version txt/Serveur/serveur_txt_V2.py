import socket, threading

class TreadForClient(threading.Thread):
    def __init__(self, connexion):
        threading.Thread.__init__(self)
        self.connexion = connexion
        connexion.send('OK'.encode("Utf8")) # Vérification de connexion
        

    def run(self):
        try: # fonctionne avec le except
            self.getPseudo()
            while True:
            
                data = self.connexion.recv(1024).decode("utf8")
                msg = self.pseudo + '> '+ data
                print(msg)
                self.sendAll(msg)
                        
        except ConnectionResetError: # Si l'utilisateur se déconnecte
            self.deconnexion()

            
    def getPseudo(self):
        self.connexion.send('Quel est ton nom ?'.encode("utf8"))
        self.pseudo = self.connexion.recv(1024).decode("utf8")
        
    def deconnexion(self):
        """
        Déconnexion du client
        """
        connexion_list.remove(self.connexion)
        self.connexion.close()
        
    def sendAll(self, msg):
        """
        envoie à tout les utilisateurs sauf celui qui l'a envoyé
        """
        for conn in connexion_list:
            if conn != self.connexion:
                conn.send(msg.encode("Utf8"))
                
                
                
                
                

host, port = '', 80

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du serveur en TCP
socket.bind((host, port))
print('Le serveur est prêt')

connexion_list = [] # Permet d'ajouter toute les connexions pour envoyer les messages

while True:
    socket.listen(5)
    connexion, address = socket.accept()
    print('Connexion de :', address)
    connexion_list.append(connexion)
    print(connexion_list)

    my_thread = TreadForClient(connexion) # Création du theard pour le client
    my_thread.start()


connexion.close()
socket.close()
