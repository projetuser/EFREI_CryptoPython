from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify, request
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>/<string:cle>')
def encryptage(valeur, cle):
    f = Fernet(cle.encode())  # Utiliser la clé fournie
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>/<string:cle>')
def decryptage(token, cle):
    f = Fernet(cle.encode())  # Utiliser la clé fournie
    token_bytes = token.encode()  # Conversion str -> bytes
    valeur_bytes = f.decrypt(token_bytes)  # Décryptage
    valeur = valeur_bytes.decode()  # Conversion bytes -> str
    return f"Valeur décryptée : {valeur}"  # Retourne la valeur décryptée

if __name__ == "__main__":
    app.run(debug=True)
