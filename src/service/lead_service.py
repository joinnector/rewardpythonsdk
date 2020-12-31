import service.base_sdk_service as base_sdk_service


class LeadService(base_sdk_service.BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def get_by_email(self, key, value):
        return super().get_by(key, value)

    def get_by_mobile(self, key, value):
        return super().get_by(key, value)


lead_service = LeadService("lead")
