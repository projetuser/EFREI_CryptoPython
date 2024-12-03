from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, render_template_string, render_template, jsonify, request
from urllib.request import urlopen
import sqlite3
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>/<string:cle>')
def encryptage(valeur, cle):
    try:
        # Validation de la clé
        if len(cle) != 44 or not base64.urlsafe_b64decode(cle.encode()):
            return "Clé invalide. Elle doit être une chaîne de 32 octets encodée en base64.", 400
        
        f = Fernet(cle.encode())  # Utiliser la clé fournie
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return str(e), 500

@app.route('/encrypt/<string:valeur>/<string:cle>')
def encryptage(valeur, cle):
    try:
        # Validation de la clé
        if len(cle) != 44 or not base64.urlsafe_b64decode(cle.encode()):
            return "Clé invalide. Elle doit être une chaîne de 32 octets encodée en base64.", 400
        
        f = Fernet(cle.encode())  # Utiliser la clé fournie
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
