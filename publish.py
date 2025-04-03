# ZMQ Publish Socket

import logging
import zmq
import struct # for packing integers

from lzerocomms import base

# Publish - Subscribe (PUB-SUB)
#
#	(localhost) Publisher sends to subscribers
#
class Publish (base.Base):
	def __init__(self, context, port):
		super(Publish, self).__init__(context, base.Base.cLocalHost, port)
		self.logger			=	logging.getLogger('Publish')
		self.socket	=	context.socket(zmq.PUB)


	def __del__(self):
		super(Publish, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Publish, self).initialise()
		# Bind the socket
		self.socket.bind(self.connectionURL)

	# Send Data
	def send(self, listOfData):
		self.logger.debug("Sending (%s) under topic\"%s\"", data, topic)
		etData = self.socket.send_multipart(listOfData)

