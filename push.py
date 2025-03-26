# ZMQ Push Socket

import logging
import zmq

from lzerocomms import base

# PIPELINE (PUSH-PULL)
#
#	Push to send data to pull clients
#
class Push (base.Base):
	def __init__(self, context, hostname, port):
		super(Push, self).__init__(context, hostname, port)
		self.logger		=	logging.getLogger('Push')
		self.socket		=	context.socket(zmq.PUSH)


	def __del__(self):
		super(Push, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Push, self).initialise()
		# Connect the socket
		self.socket.connect(self.connectionURL)
