from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import pytest

class TestGiftcardDiscountOperation():
    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server = None
    
    def test_ListProducts_without_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).discounts().List_without_filter()
        assert request!=None
        self.assertIsValidDiscountResponse(request)

    def test_ListProducts_with_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        page_size = 5
        filter = QueryFilter().withPage(1, 5)
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).discounts().List_with_filter(filter)
        assert request!=None
        assert len(request['content']) == 5
        self.assertIsValidDiscountResponse(request)

    def test_GetbyId(self):
        discountId = 3
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).discounts().getById(discountId)
        assert request!=None
        self.assertIsValidDiscountResponse(request)

    def test_GetByIdShouldThrowExceptionwhenDiscountIdIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).discounts().getById(None)

    def test_GetByIdShouldThrowExceptionWhenDiscountIdIsLessThanZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = -2342
            self.request = GiftCardAPI.discounts().getById(transactionId)
    
    def test_GetByIdShouldThrowExceptionWhenDiscountIdIsEqualToZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = 0
            self.request = GiftCardAPI.discounts().getById(transactionId)

    def assertIsValidDiscountResponse(self, discount):
        discountFields = ["product", "productId", "countryCode",
                "global", "discountPercentage"]

        for i in discount:
            count = 0
            for j in i:
                if type(j)==str:
                    assert j!=None
                elif type(j)==dict:
                    assert j[discountFields[count]]!=None
                count = count + 1