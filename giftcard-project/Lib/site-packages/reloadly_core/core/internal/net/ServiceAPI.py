import reloadly_core.core.exception.ReloadlyException as ReloadlyException
import reloadly_core.core.internal.dto.request.interfaces.Request as Request
from reloadly_core.core.internal.util.Asserter import Asserter
import reloadly_core.core.net.HttpOptions as HttpOptions
from reloadly_core.core.internal.net.API import API
import jwt
from datetime import datetime

class ServiceAPI(API):
    cacheAccessToken = True
    def ServiceAPI(self, clientId : str, clientSecret : str, accessToken : dict, enableLogging : bool, redactHeaders : list, options, enableTelemetry : bool):
        self.accessToken = accessToken
        super().__init__()
        if self.accessToken:
            self.cacheAccessToken = True

    def validateCredentials(self, clientId, clientSecret, accessToken):
        self.accessToken = accessToken
        if not (accessToken or (clientId and clientSecret)):
            raise Exception("Either a valid access Token or both client id and client secret must be provided")
        elif not self.accessToken:
            Asserter().assertNotNull(clientId, "Client id")
            Asserter().assertNotNull(clientSecret, "client secret")
        elif not(clientId and clientSecret):
            Asserter().assertNotNull(self.accessToken, "AccessToken")

    """Update the API access token to use on new calls.
     * This is useful when the token is about to expire or already has.
     *
     * @param accessToken the token to authenticate the calls with."""


    def setAccessToken(self, accessToken : str):
        Asserter().assertNotNull(accessToken, "Access token")
        self.accessToken = self.validateAccessToken(accessToken)