# Base class for server

import logging
import threading

import zmq

from python.comms import base
#import prediction_pb2.py

class Server (base.Base):
	def __init__(self, port):
		super(Server, self).__init__('*', port)
		self.logger			=	logging.getLogger('Server')
		self.live			=	True
		self.listenThread	=	None


	def __del__(self):
		super(Server, self).__del__()


	def shutdown(self):
		self.logger.info("Shutting Down server...")
		self.live = False
		# Join the thread object
		self.listenThread.join()


	# Setup the various components of the service
	def initialise(self):
		super(Server, self).initialise()	
		# 1) Create socket
			# GOTCHA: python-zmq 17.1.2-2 does not support CLIENT/SERVER
		#	WORKAROUND:	REP
		self.socket	=	self.context.socket(zmq.REP)
		# 2) Connect the socket
		self.socket.bind(self.connectionURL)
		self.logger.debug("Setting up the listening thread")
		# 3) Initialise thread
		self.listenThread = threading.Thread(target=self.listen)
		


	# Start the service
	def start(self):
		self.logger.info("Starting server...")
		# Start thread:
		self.listenThread.start()
		#	 Calls listen function
		#		receiveHandler

	# Listen handler
	def listen(self):
		self.logger.debug("Listen started")
		while(self.live):
			self.logger.debug("Awaiting data")
			data = self.socket.recv()
			self.logger.debug("Received: %s", data)
			res = self.receiveHandler(data)
			self.socket.send(res)


	# Receive Handler
	def receiveHandler(self, data):
		self.logger.info("Default receiveHandler: %s", data)	
