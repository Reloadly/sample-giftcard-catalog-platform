from reloadly_giftcard.giftcard.sdk.dto.Response.Products import Products
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation

class ProductOperations(BaseGiftCardOperation):
    END_POINT = "products"
    ISO_END_POINT = "countries"
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.baseUrl = baseUrl
        self.client = client
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)

    def List_with_filter(self, Filter):
        return super().createGetRequest(super().buildQueryFilters(Filter, self.END_POINT))

    def List_without_filter(self):
        return super().createGetRequest(super().getBuilder(self.END_POINT))

    def getById(self,productId : int):
        self.validateProductId(productId)
        builder = super().getBuilder(self.END_POINT)
        builder = builder + "/" + str(productId)
        return super().createGetRequest(str(builder))

    def getByISO(self,countryCode: str):
        self.validateCountryCode(countryCode)
        builder = super().getBuilder(self.ISO_END_POINT + "/" + str(countryCode)) + "/" + self.END_POINT
        return super().createGetRequest(str(builder))

    def validateProductId(self,productId : int):
        Asserter().assertNotNull(productId, "Product id")
        Asserter().assertGreaterThanZero(productId, "Product id")

    def validateCountryCode(self, countryCode):
        Asserter().assertNotNull(countryCode, "Country code")
    
    