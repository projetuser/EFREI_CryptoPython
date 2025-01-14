from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/exercice1')
def exercice1():
    return render_template('exercice1.html')

@app.route('/exercice2')
def exercice2():
    return render_template('exercice2.html')

@app.route('/exercice3')
def exercice3():
    return render_template('exercice3.html')

@app.route('/exercice4')
def exercice4():
    return render_template('exercice4.html')

@app.route('/svg')
def svg():
    return render_template('svg.html')

# Route pour chiffrer une valeur avec une clé privée manuelle
@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Chiffrement de la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return f"Erreur : {str(e)}", 400

# Route pour déchiffrer une valeur avec une clé privée manuelle
@app.route('/decrypt/<string:key>/<string:encrypted_val>')
def decryptage(key, encrypted_val):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        encrypted_bytes = encrypted_val.encode()  # Conversion str -> bytes
        decrypted_text = f.decrypt(encrypted_bytes).decode()  # Déchiffrement
        return f"Valeur décryptée : {decrypted_text}"
    except Exception as e:
        return f"Erreur : {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
