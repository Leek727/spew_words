from gpg import gpg_enc, gpg_dec
import getpass
import requests
import codecs

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
