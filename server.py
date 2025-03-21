# ZMQ Server Socket

import logging
import zmq

from python.comms import base

# Request-Reply (REQ-REP, CLIENT-SERVER)
#
#	(localhost) Server listens for connections on localhost
#
class Server (base.Base):
	def __init__(self, context, port):
		super(Server, self).__init__(context, base.Base.cLocalHost, port)
		self.logger			=	logging.getLogger('Server')
			# GOTCHA: python-zmq 17.1.2-2 does not support CLIENT/SERVER
		#	WORKAROUND:	REP
		self.socket	=	self.context.socket(zmq.REP)


	def __del__(self):
		super(Server, self).__del__()


	# Setup the various components of the service
	def initialise(self):
		super(Server, self).initialise()
		# Bind the socket
		self.socket.bind(self.connectionURL)
