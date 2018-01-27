#from readtest import *
from CardList import CardList
from Reader import Reader
reader = Reader()
cardList = CardList()

while True:
		print 'Place the card in the reader'
		card = reader.readCard()
		localOrSpotify=raw_input('Press [S] for Spotify Playlist [L] for local folder')
		if localOrSpotify== "S" or "s":
			plist=raw_input('Specify Spotify URI, q to quit')
			if plist=="q":
				break
		if localOrSpotify== "L" or "l":
			plist=raw_input('Specify local folder path like this: file:/music/Card*/, q to quit')
			if plist=="q":
				break
		cardList.addPlaylist(card, plist)
print "Exiting"

