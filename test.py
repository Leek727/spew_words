"""import gpg
import download_resources

x = download_resources.download()
nouns = x[1]
adjectives = x[0]

with open("test.txt","w") as f:
	f.write(str(gpg.gpg_enc(pw, nouns)))

with open("test1.txt","w") as f:
	f.write(str(gpg.gpg_enc(pw, adjectives)))

print(nouns)
print(adjectives)"""
