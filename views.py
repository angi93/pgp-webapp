from wsgi import app
from flask import render_template
import gnupg
gpg = gnupg.GPG(homedir="/home/angelo/Documents/PGP")
pubkeys = gpg.list_keys()


@app.route('/')
def home():
    return render_template('index.html', str=pubkeys.uids)


@app.route('/encrypt')
def encrypt():
    return render_template('encrypt.html')


@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')