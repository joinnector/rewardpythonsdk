import hmac
from hashlib import sha256


class SecurityClient(object):
    def process_hmac_signature(self, value, password):
        return hmac.new(password.encode('utf8'), value.encode('utf8'), sha256).hexdigest()
