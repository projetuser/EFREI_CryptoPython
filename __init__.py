# Importation des bibliothèques nécessaires
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import paramiko

# Génération des clés publique et privée
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Sérialisation des clés
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Sauvegarde des clés dans des fichiers
with open("private_key.pem", "wb") as f:
    f.write(private_key_pem)

with open("public_key.pem", "wb") as f:
    f.write(public_key_pem)

# Connexion au serveur et dépôt de la clé publique
hostname = "votre_serveur"
port = 22
username = "votre_utilisateur"
password = "votre_mot_de_passe"

# Création de l'objet SSHClient
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connexion au serveur
client.connect(hostname, port, username, password)

# Dépôt de la clé publique
sftp = client.open_sftp()
sftp.put("public_key.pem", "/chemin/vers/le/serveur/public_key.pem")
sftp.close()

# Fermeture de la connexion
client.close()
