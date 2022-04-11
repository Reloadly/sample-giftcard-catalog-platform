# test_with_pytest.py
from reloadly_giftcard.giftcard.sdk.client.GiftcardAPI import GiftCards
from reloadly_giftcard.giftcard.tests.GiftCardAPIMockServer import GiftCardAPIMockServer
import os
import pytest
from dotenv import load_dotenv

load_dotenv('.env')

class TestgiftcardAPI():
    accessToken = os.environ.get('GIFTCARD_ACCESS_TOKEN')

    def setUp(self):
        self.server = GiftCardAPIMockServer()

    def tearDown(self):
        self.server.stop()

    def test_shouldEnableTelemetryByDefault(self):
        giftcardAPI = GiftCards(accessToken=self.accessToken)
        field = giftcardAPI.enableTelemetry
        assert field==True

    def test_shouldEnableTelemetryExplicitly(self):
        giftcardAPI = GiftCards(accessToken = self.accessToken, enableTelemetry = True)
        field = giftcardAPI.enableTelemetry
        assert field==True

    def test_shouldDisableTelemetry(self):
        giftcardAPI = GiftCards(accessToken = self.accessToken, enableTelemetry=False)
        field = giftcardAPI.enableTelemetry
        assert field==False

    def test_shouldDisableLoggingByDefault(self):
        giftcardAPI = GiftCards(accessToken = self.accessToken)
        field = giftcardAPI.enablelogging
        assert field==False

    def test_shouldEnableLogging(self):
        giftcardAPI = GiftCards(accessToken = self.accessToken , enablelogging = True)
        field = giftcardAPI.enablelogging
        assert field==True

    def test_shouldDisableLoggingInterceptorExplicitly(self):
        giftcardAPI = GiftCards(accessToken = self.accessToken , enablelogging=False)
        field = giftcardAPI.enablelogging
        assert field==False

    def test_shouldThrowExceptionWhenCredentialsAndAccessTokenAreMissing(self):
        with pytest.raises(Exception):
            giftcardAPI = GiftCards()
            