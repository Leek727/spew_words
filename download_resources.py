import requests
import codecs

def download():
	print("Downloading resources... ")
	
	
	link1 = str(input("Input link 1: "))
	link2 = str(input("Input link 2: "))
	pastebin_links = [link1,link2]

	content = []
	for flink in pastebin_links:
		r = requests.get(flink)
		content.append(r.text)

	print("Decoding... ")
	content[1] = codecs.encode(content[1],"rot-13")	
	
	print("Finished.")
	return content
