from mpd import MPDClient
from Reader import Reader

import sys
import time


def connectMPD():
	try:
		client = MPDClient()               # create client object
		client.timeout = 200               # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None
		client.connect("localhost", 6600)
		return client
	except:
		print 'Could not connect to MPD server'

def play(client, plist):
	try:
		client.stop()
		client.clear()

		client.add(plist)

		client.play()
	except:
		print 'Could not play playlist %s' % plist


reader = Reader()
client = None
before_card = None
while not client:
	client = connectMPD()
	if not client:
		time.sleep(2)

print 'Ready: place a card on top of the reader'

while True:
	try:
		card = reader.readCard()
		print 'Read card', card

		if card != '' and card != before_card:
			client = connectMPD()
			play(client, card)
			client.close()
			before_card = card
		elif card == before_card:
			print "Same card. sleep 5sec"
			time.sleep(5)

	except KeyboardInterrupt:
		sys.exit(0)

	except ValueError:
		print "this card is new"
		print "need to Set a new playlist"
                #add_card()
		time.sleep(60)

	except:
		pass
