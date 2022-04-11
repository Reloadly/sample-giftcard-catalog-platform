from reloadly_giftcard.giftcard.sdk.dto.Response.Transaction import Transactions
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation

class TransactionHistoryOperations(BaseGiftCardOperation):
    TOPUP_TRANSACTION_HISTORY_END_POINT = "reports/transaction"
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.client = client
        self.baseUrl = baseUrl
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)

    def List_without_filter(self):
        return super().createGetRequest(super().getBuilder(self.TOPUP_TRANSACTION_HISTORY_END_POINT))

    def List_with_filter(self, Filter):
        return super().createGetRequest(super().buildQueryFilters(Filter, self.TOPUP_TRANSACTION_HISTORY_END_POINT))

    def getById(self, transactionId : int):
        Asserter().assertNotNull(transactionId, "Transaction id")
        Asserter().assertGreaterThanZero(transactionId, "Transaction id")
        return super().createGetRequest(super().getBuilder(self.TOPUP_TRANSACTION_HISTORY_END_POINT) + "/" + str(transactionId))