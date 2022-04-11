from reloadly_core.core.enums.Service import Service
from reloadly_core.core.internal.net.API import API
from reloadly_core.core.internal.util.Asserter import Asserter
import reloadly_core.core.net.HttpOptions as HttpOption
from reloadly_auth.authentication.client.OAuth2ClientCredentialsOperation import OAuth2ClientCredentialsOperation
import requests

class AuthenticationAPI(API):

    BASE_URL = "https://auth.reloadly.com"
    def __init__(self):
        self.baseUrl = ""
        self.service = Service()

    def AuthenticationAPI(self, clientId, clientSecret, enableLogging = False, redactHeaders = [], options = HttpOption, enableTelemetry = True):
        super().API(clientId, clientSecret, enableLogging, redactHeaders, options, enableTelemetry)
        Asserter().assertNotEmpty(clientId,"Client id")
        Asserter().assertNotEmpty(clientSecret, "Client secret")
        Asserter().assertNotNull(self.service, "Target service")
        self.baseUrl = super().createUrlFromString(self.BASE_URL)
        if not self.baseUrl:
            raise Exception("The auth base url had an invalid format and could not be parsed as a Url")

    def clientCredentials(self, clientId, clientSecret, service):
        self.baseUrl = service
        return OAuth2ClientCredentialsOperation(self.baseUrl, clientId, clientSecret)

    
