import sys, threading, socket

class ThreadForRead(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket


    def run(self):
        while True:
            try:
                msgServeur = self.socket.recv(1024).decode("Utf8")
                print(msgServeur)
            except ConnectionResetError: # si le serveur plante, la connexion se ferme
                self.socket.close()
                break
                
            

class ThreadForWrite(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            try:
                msg = input()
                print("moi> " + msg) # print ici car le serveur ne lui envoie pas, + opti
                self.socket.send(msg.encode("Utf8"))
            except: # si le serveur plante, la connexion se ferme
                self.socket.close()
                break



HOST = "localhost"
PORT = 80


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du socket

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


my_thread_read = ThreadForRead(mySocket)
my_thread_read.start()

my_thread_write = ThreadForWrite(mySocket)
my_thread_write.start()
