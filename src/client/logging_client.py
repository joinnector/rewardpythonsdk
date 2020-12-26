import logging

import helper.constant_helper as constant_helper


class LoggingClient(object):
	'''

	'''

	def __init__(self):
		logging.basicConfig(
			format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=10)

	def process_ie_log(self, **kwargs):
		kwargs.update(
			{"service": constant_helper.ConstantHelper.get_setting_constant().SERVICE_NAME})
		getattr(logging, kwargs.get("level", "debug"))(
			**kwargs, stack_info=True)
