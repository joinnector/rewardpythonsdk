import service.base_sdk_service as base_sdk_service


class NotificationService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

notification_service = NotificationService("notification")