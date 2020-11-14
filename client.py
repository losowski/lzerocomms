# Base class for client 

import logging
import zmq

from python.comms import base

class Client (base.Base):
	def __init__(self, hostname, port):
		super(Client, self).__init__(hostname, port)
		self.logger			=	logging.getLogger('Client')
		#Default connection as client

	def __del__(self):
		super(Client, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Client, self).initialise()	
		# 1) Create socket
		# GOTCHA: python-zmq 17.1.2-2 does not support CLIENT/SERVER
		#	WORKAROUND:	REQ
		self.socket	=	self.context.socket(zmq.REQ)
		# 2) Connect the socket
		self.socket.connect(self.connectionURL)
	
