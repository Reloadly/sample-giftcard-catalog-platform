from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import pytest


class TestGiftcardOrderOperation():
    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server = None

    def test_NewGiftCardOrder(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        params = {
            "productId": 120,
            "countryCode": "US",
            "quantity": 1,
            "unitPrice": 59.99,
            "customIdentifier": "obucks15",
            "senderName": "Jane Doe",
            "recipientEmail": "anyone@email.com"
        }
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).order().send(params)
        assert request!=None

    # def test_RedeemCodeForNewOrder(self):
    #     transactionId = 574
    #     self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
    #     request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).order().getCode(transactionId)
    #     assert request!=None

    def test_GetCodeCodeShouldThrowExceptionwhenTransactionIdIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).order().getCode(None)

    def test_GetCodeShouldThrowExceptionWhenTransactionIdIsLessThanZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = -2342
            request = GiftCardAPI.order().getCode(transactionId)
    
    def test_GetCodeShouldThrowExceptionWhenTransactionIdIsEqualToZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = 0
            request = GiftCardAPI.order().getCode(transactionId)