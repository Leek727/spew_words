import gnupg

gpg = gnupg.GPG()

def gpg_enc(pw, d):
    return gpg.encrypt(symmetric=True, passphrase=pw, data=d, recipients=False)

def gpg_dec(pw,d):
    return gpg.decrypt(passphrase=pw,message=str(d))