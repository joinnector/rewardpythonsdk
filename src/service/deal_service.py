import src.service.base_sdk_service as base_sdk_service


class DealService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

	def reward(self, payload):
		return super().create(payload)

deal_service = DealService("deal")