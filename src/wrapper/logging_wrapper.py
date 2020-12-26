import client.logging_client as logging_client

class LoggingWrapper(object):
	'''

	'''
	def init(self):
		self.process_common_wrapper()

	def process_common_wrapper(self):
		self.logging_client = logging_client.LoggingClient()

	def get_wrapper(self):
		return self.logging_client


logging_wrapper = LoggingWrapper()