import src.service.base_sdk_service as base_sdk_service


class LeadService(base_sdk_service.BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def get_by_email(self, email, swap_id=None):
        return super().get_by("email", email, swap_id)

    def get_by_mobile(self, mobile, swap_id=None):
        return super().get_by("mobile", mobile, swap_id)


lead_service = LeadService("lead")
