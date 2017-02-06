from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("messages.htm"), "lxml")
message_threads = soup.find_all('p')


# get all the messages into an array object
messages = []
for message in message_threads:
	messages = messages + message.contents

with open('input.txt', 'w') as fp:
	json.dump(messages, fp)

print("In total, " + str(len(messages)) + " threads.")