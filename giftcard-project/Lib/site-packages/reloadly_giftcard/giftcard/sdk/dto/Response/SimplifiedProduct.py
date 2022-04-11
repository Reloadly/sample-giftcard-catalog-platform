from reloadly_giftcard.giftcard.sdk.dto.Response.Brand import Brand

class SimplifiedProduct():

    def __init__(self):
        self.productId = 0
        self.productName = ''
        self.countryCode = ''
        self.quantity = 0
        self.unitPrice = 0.0
        self.totalPrice = 0.0
        self.currencyCode = ''
        self.brand = Brand()
        