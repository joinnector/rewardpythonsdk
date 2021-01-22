import src.service.base_sdk_service as base_sdk_service


class WalletService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

wallet_service = WalletService("wallet")