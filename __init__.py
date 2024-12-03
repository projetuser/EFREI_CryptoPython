from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify, request
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

# Clé de chiffrement/déchiffrement
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt', methods=['POST'])
def decryptage():
    data = request.get_json()
    token = data.get('token')
    if token:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_bytes = f.decrypt(token_bytes)  # Décryptage
        valeur = valeur_bytes.decode()  # Conversion bytes -> str
        return jsonify({"valeur_decryptee": valeur})
    return jsonify({"error": "Token non fourni"}), 400

if __name__ == "__main__":
    app.run(debug=True)
