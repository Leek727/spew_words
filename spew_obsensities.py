warning = """
# # # # # # # # # # # # # # # # # # # # # # # # 
    WARNING - OFFENSIVE CONTENT AHEAD
THIS PROGRAM HAS BEEN MADE TO SPEW OBSENITITIES
                    THANKS
# # # # # # # # # # # # # # # # # # # # # # # #  
"""
print(warning)

from random import choice, randint
from time import sleep
import random
import datetime
from download_resources import download

content = download() # 
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