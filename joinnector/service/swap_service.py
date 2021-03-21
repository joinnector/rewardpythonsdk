# pylint: disable=useless-super-delegation

from joinnector.service.base_sdk_service import BaseSDKService


class SwapService(BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def get_by_sku(self, sku):
        return super().get_by("sku", sku)


swap_service = SwapService("swap")
