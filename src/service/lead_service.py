import service.base_sdk_service as base_sdk_service


class LeadService(base_sdk_service.BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def get_by_email(self, value):
        return super().get_by("email", value)

    def get_by_mobile(self, value):
        return super().get_by("mobile", value)


lead_service = LeadService("lead")
