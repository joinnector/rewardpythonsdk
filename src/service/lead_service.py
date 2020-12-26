import service.base_sdk_service as base_sdk_service


class LeadService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

lead_service = LeadService("lead")