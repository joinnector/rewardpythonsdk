# client
import wrapper.security_wrapper as security_wrapper
import wrapper.logging_wrapper as logging_wrapper
import wrapper.request_wrapper as request_wrapper

# service
import service.coupon_service as coupon_service
import service.currency_service as currency_service
import service.deal_service as deal_service
import service.lead_service as lead_service
import service.notification_service as notification_service
import service.review_service as review_service
import service.setting_service as setting_service
import service.swap_service as swap_service
import service.task_service as task_service
import service.taskactivity_service as taskactivity_service
import service.wallet_service as wallet_service
import service.wallettransaction_service as wallettransaction_service

class NectorSDK(object):
	def __init__(self, key, secret):
		self.init_wrappers(key=key, secret=secret)

	def init_wrappers(self, key, secret):
		security_wrapper.sucurity_wrapper.init()
		logging_wrapper.logging_wrapper.init()
		request_wrapper.request_wrapper.init(key=key, secret=secret)

	def get_coupon_service(self):
		return coupon_service.coupon_service

	def get_currency_service(self):
		return currency_service.currency_service

	def get_deal_service(self):
		return deal_service.deal_service

	def get_lead_service(self):
		return lead_service.lead_service

	def get_notification_service(self):
		return notification_service.notification_service

	def get_review_service(self):
		return review_service.review_service

	def get_setting_service(self):
		return setting_service.setting_service

	def get_swap_service(self):
		return swap_service.swap_service

	def get_task_service(self):
		return task_service.task_service

	def get_taskactivity_service(self):
		return taskactivity_service.taskactivity_service

	def get_wallet_service(self):
		return wallet_service.wallet_service

	def get_wallettransaction_service(self):
		return wallettransaction_service.wallettransaction_service
