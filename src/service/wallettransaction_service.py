import src.service.base_sdk_service as base_sdk_service


class WalletTransactionService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

wallettransaction_service = WalletTransactionService("wallettransaction")