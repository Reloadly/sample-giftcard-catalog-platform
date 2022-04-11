from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import pytest


class TestGiftcardTransactionHistoryOperations():
    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server = None

    def test_ListProducts_without_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).reports().transactionHistory().List_without_filter()
        assert request!=None
        self.assertIsValidTransactionHistory(request)

    def test_ListProducts_with_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        page_size = 5
        filter = QueryFilter().withPage(1, 5)
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).reports().transactionHistory().List_with_filter(filter)
        assert request!=None
        self.assertIsValidTransactionHistory(request)

    def test_GetbyId(self):
        transactionId = 573
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).reports().transactionHistory().getById(transactionId)
        assert request!=None
        self.assertIsValidTransactionHistory(request)

    def test_GetByIdShouldThrowExceptionwhenTransactiondIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).reports().transactionHistory().getById(None)

    def test_GetByTransactionIdShouldThrowExceptionWhenTransactionIdIsLessThanZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = -2342
            self.request = GiftCardAPI.reports().transactionHistory().getById(transactionId)
    
    def test_GetByTransactionIdShouldThrowExceptionWhenTransactionIdIsEqualToZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = 0
            self.request = GiftCardAPI.reports().transactionHistory().getById(transactionId)

    def assertIsValidTransactionHistory(self, transactionHistory):
        transactionFields = ["tranasactionId", "amount", "discount",
                "currencyCode", "fee", "recipientEmail", "customIdentifier", "status", "transactionCreatedTime",
                "product", "productId", "productName", "countryCode",
                "quantity", "unitPrice", "totalPrice", "currencyCode", "brand", "brandId", "brandName"]

        for i in transactionHistory:
            count = 0
            for j in i:
                if type(j)==str:
                    assert j!=None
                elif type(j)==dict:
                    assert j[transactionFields[count]]!=None
                count = count + 1
      