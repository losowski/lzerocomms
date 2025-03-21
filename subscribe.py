# ZMQ Subscribe Socket

import logging
import zmq

from lzerocomms import base

# Publish - Subscribe (PUB-SUB)
#
#	Subscriber receives data from a known publisher
#
class Subscribe (base.Base):
	def __init__(self, context, hostname, port):
		super(Subscribe, self).__init__(context, hostname, port)
		self.logger		=	logging.getLogger('Subscribe')
		self.socket		=	context.socket(zmq.SUB)


	def __del__(self):
		super(Server, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Server, self).initialise()
		# Connect the socket
		self.socket.connect(self.connectionURL)
