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
		super(Publish, self).__init__(context, base.Base.cLocalHost, port)
		self.logger			=	logging.getLogger('Publish')
		self.socket	=	self.context.socket(zmq.PUB)


	def __del__(self):
		super(Client, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Client, self).initialise()
		# Bind the socket
		self.socket.bind(self.connectionURL)
