from reloadly_giftcard.giftcard.sdk.dto.Response.RedeemInstructions import RedeemInstructions
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation

class RedeemOperations(BaseGiftCardOperation):
    END_POINT = "redeem-instructions"
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.baseUrl = baseUrl
        self.client = client
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)

    def List(self):
        return super().createGetRequest(super().getBuilder(self.END_POINT))

    def getById(self,brandId : int):
        self.validateBrandId(brandId)
        builder = super().getBuilder(self.END_POINT + "/" + str(brandId))
        return super().createGetRequest(str(builder))

    def validateBrandId(self,brandId : int):
        Asserter().assertNotNull(brandId, "Brand id")
        Asserter().assertGreaterThanZero(brandId, "Brand id")