# ZMQ Pull Socket

import logging
import zmq

from python.comms import base

# PIPELINE (PUSH-PULL)
#
#	(localhost) Pull to receive data from push clients
#
class Pull (base.Base):
	def __init__(self, context, port):
		super(Pull, self).__init__(context, base.Base.cLocalHost, port)
		self.logger		=	logging.getLogger('Pull')
		self.socket		=	self.context.socket(zmq.PULL)


	def __del__(self):
		super(Server, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Server, self).initialise()
		# Bind the socket
		self.socket.bind(self.connectionURL)
