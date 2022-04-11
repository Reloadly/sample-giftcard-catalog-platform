from reloadly_giftcard.giftcard.sdk.dto.Response.Discount import Discount
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation

class DiscountOperations(BaseGiftCardOperation):
    END_POINT = "discounts"
    FETCH_PATH = "products"
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.baseUrl = baseUrl
        self.client = client
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)

    def List_with_filter(self, Filter):
        return super().createGetRequest(super().buildQueryFilters(Filter, self.END_POINT))

    def List_without_filter(self):
        return super().createGetRequest(super().getBuilder(self.END_POINT))

    def getById(self,productID : int):
        self.validateProductId(productID)
        builder = super().getBuilder(self.FETCH_PATH + "/" + str(productID)) + "/" + self.END_POINT
        return super().createGetRequest(str(builder) )

    def validateProductId(self,productID : int):
        Asserter().assertNotNull(productID, "Operator id")
        Asserter().assertGreaterThanZero(productID, "Operator id")
        