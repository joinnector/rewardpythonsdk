import service.base_sdk_service as base_sdk_service


class TaskActivityService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

taskactivity_service = TaskActivityService("taskactivity")