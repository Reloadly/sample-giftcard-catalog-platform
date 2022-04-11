from reloadly_giftcard.giftcard.sdk.operation.BaseGiftCardOperation import BaseGiftCardOperation
from reloadly_giftcard.giftcard.sdk.operation.TransactionHistoryOperations import TransactionHistoryOperations

class ReportOperations(BaseGiftCardOperation):
    def __init__(self, client, baseUrl : str, apiToken : str):
        self.client = client
        self.baseUrl = baseUrl
        self.apiToken = apiToken
        super().__init__(self.client, self.baseUrl, self.apiToken)


    def transactionHistory(self):
        return TransactionHistoryOperations(self.client, self.baseUrl, self.apiToken)