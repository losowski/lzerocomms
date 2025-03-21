# ZMQ Client Socket

import logging
import zmq

from python.comms import base

# Request-Reply (REQ-REP, CLIENT-SERVER)
#
#	Client connects to a known host
#
class Client (base.Base):
	def __init__(self, context, hostname, port):
		super(Client, self).__init__(context, hostname, port)
		self.logger		=	logging.getLogger('Client')
		# GOTCHA: python-zmq 17.1.2-2 does not support CLIENT/SERVER
		#	WORKAROUND:	REQ
		self.socket		=	self.context.socket(zmq.REQ)

	def __del__(self):
		super(Client, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Client, self).initialise()
		# Connect the socket
		self.socket.connect(self.connectionURL)
