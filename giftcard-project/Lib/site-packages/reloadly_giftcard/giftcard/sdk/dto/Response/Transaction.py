from reloadly_giftcard.giftcard.sdk.dto.Response.SimplifiedProduct import SimplifiedProduct

class Transactions():

    def __init__(self):
        self.tranasactionId = 0
        self.amount = 0.0
        self.discount = 0.0
        self.currencyCode = ''
        self.fee = 0.0
        self.recipientEmail = ''
        self.customIdentifier = ''
        self.status = ''
        self.product = SimplifiedProduct()
        self.transactionCreatedTime = None
