# Flask with Gnupg
This webapp give you the possibilities to manage your PGP keys with the following operations:

- Create new key
- Delete a key
- Encrypt your message with your public key
- Decrypt your message with your private key

Basically this webapp is a wrapper of gnupg library. For more info see the documentation https://pythonhosted.org/gnupg/gnupg.html



### Installation

Download from any of the following sources depending on your operating system:

- https://www.gpg4win.org/ for Windows
- https://www.gpgtools.org/ for OS X

If you are using Linux then use your package manager. e.g for Ubuntu:

```
$ sudo apt-get install gnupg
$ sudo apt-get install rng-tools
```



### Run the webapp

For start the webapp type on your console 

```
$  python3 wsgy.py
```

Now open a browser and go to the following URL: http://localhost:5000

You should see the home page