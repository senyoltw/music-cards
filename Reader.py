import sys
import nfc
import nfc.ndef

class Reader:

	def startup(self, targets):
		print "waiting for new NFC tags..."
		return targets

	def released(self, tag):
		print("released:")
		return tag

	def connected_read(self, tag):
		if not tag.ndef or not tag.ndef.is_writeable:
        		print("not a writeable nfc tag")
        		return False
    		print 'data:', nfc.ndef.TextRecord(tag.ndef.message[0]).text

	def connected_write(self, tag):
		if not tag.ndef or not tag.ndef.is_writeable:
			print("not a writeable nfc tag")
                        return False
		try:
                	print 'old data:', nfc.ndef.TextRecord(tag.ndef.message[0]).text
		except ValueError:
			print "this NFC is NEW"

		record = nfc.ndef.TextRecord(self.text)
		new_message = nfc.ndef.Message(record)

		if len(str(new_message)) > tag.ndef.capacity:
			print "too long message"
			return False

		if tag.ndef.message == new_message:
			print "already same record"
			return True

		tag.ndef.message = new_message
		print 'new data:', nfc.ndef.TextRecord(tag.ndef.message[0]).text

		print "release your NFC"


	def readCard(self):
		rdwr_options = {
			'on-startup': self.startup,
			'on-connect': self.connected_read,
		}
		with nfc.ContactlessFrontend('usb') as clf:
			tag = clf.connect(rdwr=rdwr_options)
			if tag.ndef:
				return(nfc.ndef.TextRecord(tag.ndef.message[0]).text)
			else:
				return False

        def writeCard(self, text):
                self.text = text
		rdwr_options = {
                        'on-startup': self.startup,
                        'on-connect': self.connected_write,
                }
                with nfc.ContactlessFrontend('usb') as clf:
                        tag = clf.connect(rdwr=rdwr_options)
                        if tag.ndef:
                                return(nfc.ndef.TextRecord(tag.ndef.message[0]).text)
                        else:
                                return False

	def released_Card(self):
		rdwr_options = {
			'on-release': self.released,
		}
		with nfc.ContactlessFrontend('usb') as clf:
			tag = clf.connect(rdwr=rdwr_options)
			if tag.ndef:
				return(nfc.ndef.TextRecord(tag.ndef.message[0]).text)
			else:
				return False
