# ZMQ Subscribe Socket

import logging
import zmq

from python.comms import base

# Publish - Subscribe (PUB-SUB)
#
#	Subscriber receives data from a known publisher
#
class Subscribe (base.Base):
	def __init__(self, context, hostname, port):
		super(Server, self).__init__(context, hostname, port)
		self.logger			=	logging.getLogger('Subscribe')


	def __del__(self):
		super(Server, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Server, self).initialise()
		# 1) Create socket
		self.socket	=	self.context.socket(zmq.SUB)
		# 2) Connect the socket
		self.socket.bind(self.connectionURL)
