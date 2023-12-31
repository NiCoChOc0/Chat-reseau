import sys, socket
from thread_perso import ThreadForRead, ThreadForWrite
from affichage import Fenetre

pseudo = input('Quel est ton pseudo ?')

HOST = "localhost"
PORT = 80

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création du socket

# Débugage si la connexion échoue
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")


# Système de vérification
msgServeur = mySocket.recv(1024).decode("Utf8")
if msgServeur != 'OK':
    print('Erreur')
    sys.exit()

print('Connection réussie')

# Création des threads
my_thread_read = ThreadForRead(mySocket)
my_thread_read.start()

my_thread_write = ThreadForWrite(mySocket, pseudo)
my_thread_write.start()

Fenetre(my_thread_read, my_thread_write)