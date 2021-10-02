from random import choice, randint
from time import sleep
import random
import datetime
import getpass
import requests
import codecs
import gnupg

gpg = gnupg.GPG()

def gpg_dec(pw,d):
    return gpg.decrypt(passphrase=pw,message=str(d))


def download():
	print("Downloading resources... ")
	
	pastebin_links = ["https://pastebin.com/raw/2ns0hxRY","https://pastebin.com/raw/S3FdBhQE"]

	pw = getpass.getpass(prompt='Password: ', stream=None)

	content = []
	for flink in pastebin_links:
		r = requests.get(flink)
		content.append(r.text)

	print("Decrypting... ")
	content[0] = str(gpg_dec(pw,content[0]))
	content[1] = str(gpg_dec(pw,content[1]))	
	
	print("Finished.")
	return content


content = download()
adjectives = content[1].replace("\r","").split("\n")[:-1]
nouns = content[0].split(", ")

seed = str(input("Type seed or generate a new one? (a - seed, b - generate) : "))
if seed == "a":
	x = str(input("Type seed : "))

else:
	print("Generating... ")
	x = str(random.randint(1,1000000000000000)) + str(datetime.datetime.now())

random.seed(x)
print(f"seed : {x}")
i = 0
while True:
	print(str(i) + '  ' + choice(adjectives) + ' ' + choice(nouns))
	sleep(.15)
	i += 1