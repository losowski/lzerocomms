# Base class for prediction server

import logging
import zmq

class Base (object):
	cConnectionURL	=	"{protocol}://{hostname}:{port}"
	cLocalHost		=	"localhost"

	def __init__(self, context, hostname, port):
		self.logger			=	logging.getLogger('Base')
		#Default connection as client
		self.protocol		=	'tcp'
		self.hostname		=	hostname
		self.port			=	port
		self.connectionURL	=	Base.cConnectionURL.format(protocol = self.protocol, hostname = self.hostname, port = self.port)
		self.context		=	context
		self.socket			=	None
		self.logger.info("Connection: %s", self.connectionURL)


	def __del__(self):
		self.logger.info("Shutting down..")
		if (None != self.socket):
			self.logger.info("Closing socket")
			self.socket.close()


	def initialise(self):
		self.logger.info("Initialising")
		# 1) Create socket
		# 2) Connect the socket


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
