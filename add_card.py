import re
from Reader import Reader
reader = Reader()

def add_card():
	while True:
		print 'Place the card in the reader or press CTRL+C to quit'
		try:
			card = reader.readCard()
		except ValueError:
			print "thin card in maybe notdata"

		print 'Specify path like this: file:/music/Card*/, q to quit'
		plist=raw_input('this: ')
		if plist=="q":
			break

		if re.compile("spotify").match(plist):
			plist=plist.replace("spotify:playlist", "spotify:user:user:playlist", 1)
			print "replace for spotify"
			print(plist)

		reader.writeCard(plist)

	print "Exiting"

if __name__ == '__main__':
	add_card()
