import client.request_client as request_client

class RequestWrapper(object):
	'''

	'''
	def init(self, key, secret):
		self.process_common_wrapper(key, secret)

	def process_common_wrapper(self, key, secret):
		self.request_client = request_client.RequestClient(key=key, secret=secret)

	def get_wrapper(self):
		return self.request_client


request_wrapper = RequestWrapper()