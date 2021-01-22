import src.service.base_sdk_service as base_sdk_service


class CouponService(base_sdk_service.BaseSDKService):
	def __init__(self, name):
		super().__init__(name)

coupon_service = CouponService("coupon")