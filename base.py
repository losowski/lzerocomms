# Base class for prediction server

import logging
import zmq

class Base (object):
	ConnectionURL =   "{protocol}://{hostname}:{port}"

	def __init__(self, hostname, port):
		self.logger			=	logging.getLogger('Base')
		#Default connection as client
		self.protocol		=	'tcp'
		self.hostname		=	hostname
		self.port			=	port
		self.connectionURL	=	Base.ConnectionURL.format(protocol = self.protocol, hostname = self.hostname, port = self.port)
		self.context		=	zmq.Context()
		self.socket			=	None
		self.logger.info("Connection: %s", self.connectionURL)


	def __del__(self):
		self.logger.info("Shutting down..")
		if (None != self.socket):
			self.logger.info("Closing socket")
			self.socket.close()
		if (None != self.context):
			self.logger.info("Closing Context")
			self.context.term()
			self.context.destroy()


	# Setup the various components of the service
	def initialise(self):
		self.logger.info("Initialising the Service")
		# 1) Create socket
		# 2) Connect the socket

	# Start the service
	def start(self):
		self.logger.info("Starting the service")
		# Implement this in the base class

	# Send Data
	def send(self, data):
		self.logger.debug("Sending (%s)....", data)
		self.socket.send(data)

	# Receive Data
	def receive(self):
		self.logger.debug("Receiving....")
		data = self.socket.recv()
		self.logger.debug("Received (%s)....", data)
		return data
