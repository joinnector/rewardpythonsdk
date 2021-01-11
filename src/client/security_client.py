import hmac
import hashlib
import urllib.parse

class SecurityClient(object):
	'''

	'''

	def process_hmac_signature(self, value, password):
		return hmac.new(password.encode('utf8'), value.encode('utf8'), hashlib.sha256).hexdigest()
