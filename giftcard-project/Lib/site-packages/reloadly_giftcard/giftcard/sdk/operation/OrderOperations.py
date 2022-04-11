from reloadly_giftcard.giftcard.sdk.dto.Response.Transaction import Transactions
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation

class OrderOperations(BaseGiftCardOperation):
    END_POINT = "orders"
    TRANSACTION_PATH = "transactions"
    CARD_PATH = "cards"
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.client = client
        self.baseUrl = baseUrl
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)

    def send(self, request):
        self.validateOrderRequest(request)
        return super().createPostRequest(super().getBuilder(self.END_POINT), request)

    def getCode(self, transactionId: int):
        self.validateTransactionId(transactionId)
        builder = super().getBuilder(self.END_POINT + "/" + self.TRANSACTION_PATH + "/" + str(transactionId) + "/" + self.CARD_PATH) 
        return super().createGetRequest(str(builder))
        

    def validateTransactionId(self, transactionId: int):
        Asserter().assertNotNull(transactionId, "Transaction Id")
        Asserter().assertGreaterThanZero(transactionId, "Transaction Id")

    def validateOrderRequest(self,request):
        Asserter().assertNotNull(request["unitPrice"], "unitPrice")
        Asserter().assertGreaterThanZero(request["unitPrice"], "unitPrice")
        Asserter().assertNotNull(request["quantity"], "quantity")
        Asserter().assertGreaterThanZero(request["quantity"], "quantity")
        Asserter().assertNotNull(request["productId"], "Product Id")
        Asserter().assertGreaterThanZero(request["productId"], "Product id")
        Asserter().assertNotNull(request["customIdentifier"], "customIdentifier")
        Asserter().assertValidEmail(request["recipientEmail"], "RecepientEmail")

    # todo, add redeem card codes here.
