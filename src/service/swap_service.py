import service.base_sdk_service as base_sdk_service


class SwapService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

swap_service = SwapService("swap")