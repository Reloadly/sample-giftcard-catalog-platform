from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import pytest

class TestRedeemOperations():
    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server = None

    def test_List_Redeem_Instructions(self):
        self.baseUrlField = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).baseUrl
        request = GiftCards(clientId=GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret).redeem_instructions().List()
        assert request!=None

    def test_GetByIdShouldThrowExceptionwhenIdIsNull(self):
        with pytest.raises(Exception):
            self.giftcardAPI = GiftCards(accessToken=GiftCardAPIMockServer().accessToken).redeem_instructions().getById(None)

    def test_GetByIdShouldThrowExceptionWhenIdIsLessThanZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            brandId = -2342
            self.request = GiftCardAPI.redeem_instructions().getById(brandId)
    
    def test_GetByIdShouldThrowExceptionWhenIdIsEqualToZero(self):
        with pytest.raises(Exception):
            GiftCardAPI = GiftCards(clientId = GiftCardAPIMockServer().clientId, clientSecret=GiftCardAPIMockServer().clientSecret)
            brandId = 0
            self.request = GiftCardAPI.redeem_instructions().getById(brandId)

    def assertIsValidRedeemResponse(self, redeem):
        brandId = redeem['brandId']
        brandName = redeem['brandName']
        concise = redeem['concise']
        verbose = redeem['verbose']
        assert brandId!=None
        assert brandName!=None
        assert concise!=None
        assert verbose!=None