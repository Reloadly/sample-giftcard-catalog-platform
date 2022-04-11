from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import pytest

class TestProductOperations():
    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server = None

    def test_ListProducts_without_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).products().List_without_filter()
        assert request!=None
        self.assertIsValidProduct(request)

    def test_ListProducts_with_filter(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        page_size = 5
        filter = QueryFilter().withPage(1, 5)
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).products().List_with_filter(filter)
        assert request!=None
        self.assertIsValidProduct(request)

    def test_GetbyId(self):
        productId = 10
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).products().getById(productId)
        assert request!=None
        self.assertIsValidProduct(request)

    def test_GetByISOCodeShouldThrowExceptionwhenCountryCodeIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).products().getByISO_without_filter(None)

    def test_GetByIdCodeShouldThrowExceptionwhenProductIdIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).products().getById(None)

    def test_GetByProductIdShouldThrowExceptionWhenProductIdIsLessThanZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = -2342
            request = GiftCardAPI.products().getById(transactionId)
    
    def test_GetByProductIdShouldThrowExceptionWhenProductIdIsEqualToZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            transactionId = 0
            request = GiftCardAPI.products().getById(transactionId)

    def assertIsValidProduct(self, product):
        productFields = [
            "productId", "productId","productName", "global", "senderFee", "discountPercentage", 
            "denominationType", "recipientCurrencyCode", "minRecipientDenomination", 
            "maxRecipientDenomination", "senderCurrencyCode", "minSenderDenomination", 
            "maxSenderDenomination", "fixedRecipientDenominations", "fixedSenderDenominations", 
            "fixedRecipientToSenderDenominationsMap", "logoUrls", "brand", "country", "redeemInstruction"
            ]

        for i in product:
            count = 0
            for j in i:
                if type(j)==str:
                    assert j!=None
                elif type(j)==dict:
                    assert j[productFields[count]]!=None
                count = count + 1