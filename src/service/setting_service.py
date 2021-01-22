import src.service.base_sdk_service as base_sdk_service


class SettingService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

setting_service = SettingService("setting")