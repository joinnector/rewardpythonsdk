import requests

import helper.constant_helper as constant_helper


class RequestClient(object):
	'''
	key - api key
	secret - api secret
	'''

	def __init__(self, key, secret):
		self.key = key
		self.secret = secret

	def process_axios_get(self, url, headers, params=dict()):
		headers = { **headers,  **constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER}
		return requests.get(url, headers=headers, params=params)

	def process_axios_put(self, url, headers, params=dict(), data=dict()):
		headers = { **headers,  **constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER}

		if headers["content-type"] is "application/x-www-form-urlencoded":
			headers.update({"content-type": "application/x-www-form-urlencoded"})

		return requests.put(url, headers=headers, params=params, data=data)

	def process_axios_delete(self, url, headers, params=dict()):
		headers = { **headers,  **constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER}
		return requests.delete(url, headers=headers, params=params)

	def process_axios_post(self, url, headers, params=dict(), data=dict()):
		headers = { **headers,  **constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER}

		if headers["content-type"] is "application/x-www-form-urlencoded":
			headers.update({"content-type": "application/x-www-form-urlencoded"})

		return requests.post(url, headers=headers, params=params, data=data)
