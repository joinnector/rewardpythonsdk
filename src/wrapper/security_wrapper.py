import src.client.security_client as security_client

class SecurityWrapper(object):
	'''

	'''
	def init(self):
		self.process_common_wrapper()

	def process_common_wrapper(self):
		self.security_client = security_client.SecurityClient()

	def get_wrapper(self):
		return self.security_client


sucurity_wrapper = SecurityWrapper()