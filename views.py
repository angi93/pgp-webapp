from wsgi import app
from flask import render_template
import gnupg
import json
import os

gpg = gnupg.GPG(homedir="/home/angelo/Documents/PGP")
pubkeys = gpg.list_keys()

def getConfig():
    with open(os.getcwd() + '/config.json') as data_file:
        data = data_file.read()
    return json.loads(data)

def setConfig(updatedConfig):
    with open(os.getcwd() + '/config.json', 'w') as outfile:
        json.dump(updatedConfig, outfile)


@app.route('/')
def home():
    return render_template('index.html', str=pubkeys.uids)


@app.route('/encrypt')
def encrypt():
    config = getConfig()
    print(config['homedir'])
    if config['homedir'] is None or config['homedir'] == "":
        config['homedir'] = os.getcwd()
    setConfig(config)
    return render_template('encrypt.html', config=getConfig())


@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


