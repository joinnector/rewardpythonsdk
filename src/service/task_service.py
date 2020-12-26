import service.base_sdk_service as base_sdk_service


class TaskService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

task_service = TaskService("task")