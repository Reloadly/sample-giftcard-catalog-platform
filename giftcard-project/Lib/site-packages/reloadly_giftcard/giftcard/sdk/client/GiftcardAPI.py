from reloadly_giftcard.giftcard.sdk.operation.ProductOperations import ProductOperations
from reloadly_giftcard.giftcard.sdk.operation.RedeemOperations import RedeemOperations
from reloadly_giftcard.giftcard.sdk.operation.DiscountOperations import DiscountOperations
from reloadly_giftcard.giftcard.sdk.operation.ReportOperations import ReportOperations
from reloadly_giftcard.giftcard.sdk.operation.OrderOperations import OrderOperations
from reloadly_auth.authentication.client.AuthenticationAPI import AuthenticationAPI
from reloadly_auth.authentication.client.OAuth2ClientCredentialsOperation import OAuth2ClientCredentialsOperation
from reloadly_core.core.enums.Environment import Environment
from reloadly_core.core.enums.Service import Service
import reloadly_core.core.exception.ReloadlyException as ReloadlyException
import reloadly_core.core.internal.constant.HttpHeader as HttpHeader
import reloadly_core.core.internal.dto.request.CustomizableRequest as CustomizableRequest 
import reloadly_core.core.internal.dto.request.interfaces.Request as Request
from reloadly_core.core.internal.enums.Version import Version
from reloadly_core.core.internal.net.ServiceAPI import ServiceAPI
from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_core.core.net.HttpOptions import HttpOptions
from xml.etree import ElementTree as et
from requests.compat import urljoin
import json
import requests
from datetime import datetime
from urllib3 import PoolManager, logging
import time


class GiftCards(ServiceAPI):
    
    def __init__(self, clientId = "", clientSecret = "", client = PoolManager() , accessToken = "", environment = Environment, enablelogging = False, redactHeaders = [], options = HttpOptions(), enableTelemetry = True):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.enablelogging = enablelogging
        self.enableTelemetry = enableTelemetry
        self.accessToken = accessToken
        self.environment = environment
        self.redactHeaders = redactHeaders
        self.options = options
        self.client = client
        super().ServiceAPI(clientId, clientSecret, accessToken, enablelogging, redactHeaders, options, enableTelemetry)
        self.validateCredentials(clientId, clientSecret, accessToken)
        self.environment = environment
        self.baseUrl = self.createBaseUrl()

    def refreshAccessToken(self, request):
        self.accessToken = None
        request = CustomizableRequest()
        newAccessToken = self.retrieveAccessToken()
            
        request.addHeader(HttpHeader.AUTHORIZATION,"Bearer " + newAccessToken)

    def createBaseUrl(self):
        service = self.getServiceByEnvironment(self.environment)
        Asserter().assertNotNull(service, "Service")
        if self.environment == Environment.LIVE:
            url = Service.GIFTCARD
        else:
            url = Service.GIFTCARD_SANDBOX
        if not url:
            raise Exception("The giftcard base url had an invalid format and coudnt be parsed as a Url.")
        return url

    def getServiceByEnvironment(self, environment):
        if (self.environment == environment.LIVE):
            return "GIFTCARD"
        else:
            return "GIFTCARD_SANDBOX"

    def retrieveAccessToken(self):
        if (self.accessToken):
            return self.accessToken
        return self.doGetAccessToken(self.getServiceByEnvironment(self.environment))

    def doGetAccessToken(self, service):
        try:
            if self.enablelogging:
                logging.basicConfig(level = logging.DEBUG)
            if self.accessToken:
                return self.accessToken
            else:
                return OAuth2ClientCredentialsOperation(self.baseUrl, self.clientId, self.clientSecret).getAccessToken(self.baseUrl)
        except:
            raise Exception("ReloadlyException")

    def products(self):
        try:
            a = self.retrieveAccessToken()
            return ProductOperations(self.client, self.baseUrl, a)
        except:
            raise Exception("ReloadlyException")

    def redeem_instructions(self):
        try:
            a = self.retrieveAccessToken()
            return RedeemOperations(self.client, self.baseUrl, a)
        except:
            raise Exception("ReloadlyException")

    def discounts(self):
        try:
            a = self.retrieveAccessToken()
            return DiscountOperations(self.client, self.baseUrl, a)
        except:
            raise Exception("ReloadlyException")

    def reports(self):
        try:
            a = self.retrieveAccessToken()
            return ReportOperations(self.client, self.baseUrl, a)
        except:
            raise Exception("ReloadlyException")

    def order(self):
        try:
            a = self.retrieveAccessToken()
            return OrderOperations(self.client, self.baseUrl, a)
        except:
            raise Exception("ReloadlyException")
            


        



    
            





