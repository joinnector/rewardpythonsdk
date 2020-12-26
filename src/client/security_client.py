import hmac
import hashlib
import binascii

class SecurityClient(object):
	'''

	'''

	def process_hmac_signature(self, value, password):
		byte_key = binascii.unhexlify(password)
		encoded_message = value.encode()
		return hmac.new(byte_key, encoded_message, hashlib.sha256).hexdigest()

	def process_sha256_hash(self, value):
		return hashlib.sha256(value).hexdigest()
