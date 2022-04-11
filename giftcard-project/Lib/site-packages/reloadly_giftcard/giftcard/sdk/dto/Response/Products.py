from reloadly_giftcard.giftcard.sdk.dto.Response.SimplifiedCountry import SimplifiedCountry
from reloadly_giftcard.giftcard.sdk.dto.Response.Brand import Brand
from reloadly_giftcard.giftcard.sdk.enums.DenominationType import DenominationType

class Products():

    def __init__(self):
        self.productId = 0
        self.productName = ''
        # self.global = False
        self.senderFee = 0.0
        self.discountPercentage = 0.0
        self.denominationType = DenominationType()
        self.recipientCurrencyCode = ''
        self.minRecipientDenomination = 0.0
        self.maxRecipientDenomination = 0.0
        self.senderCurrencyCode = ''
        self.minSenderDenomination = 0.0
        self.maxSenderDenomination = 0.0
        self.fixedRecipientDenominations = None
        self.fixedSenderDenominations = None
        self.fixedRecipientToSenderDenominationsMap = None
        self.logoUrls = None
        self.brand = Brand()
        self.country = SimplifiedCountry()

