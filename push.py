# ZMQ Push Socket

import logging
import zmq

from python.comms import base

# PIPELINE (PUSH-PULL)
#
#	Push to send data to pull clients
#
class Push (base.Base):
	def __init__(self, context, hostname, port):
		super(Push, self).__init__(context, hostname, port)
		self.logger		=	logging.getLogger('Push')
		self.socket		=	self.context.socket(zmq.PUSH)


	def __del__(self):
		super(Client, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Client, self).initialise()
		# Connect the socket
		self.socket.connect(self.connectionURL)
