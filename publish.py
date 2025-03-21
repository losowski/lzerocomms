# ZMQ Publish Socket

import logging
import zmq

from python.comms import base

# Publish - Subscribe (PUB-SUB)
#
#	(localhost) Publisher sends to subscribers
#
class Publish (base.Base):
	def __init__(self, context, port):
		super(Client, self).__init__(context, base.Base.cLocalHost, port)
		self.logger			=	logging.getLogger('Publish')

	def __del__(self):
		super(Client, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Client, self).initialise()
		# 1) Create socket
		self.socket	=	self.context.socket(zmq.PUB)
		# 2) Connect the socket
		self.socket.connect(self.connectionURL)
