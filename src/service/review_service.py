import service.base_sdk_service as base_sdk_service


class ReviewService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

review_service = ReviewService("review")