import reloadly_auth.authentication.dto.request.OAuth2ClientCredentialsRequest as Request
from reloadly_auth.authentication.dto.request.TokenRequest import TokenRequest
from reloadly_core.core.internal.constant.GrantType import GrantType
from reloadly_core.core.internal.constant.HttpHeader import HttpHeader
from reloadly_core.core.internal.constant.MediaType import MediaType
import reloadly_core.core.enums.Service as Service
from reloadly_core.core.internal.util.Asserter import Asserter
import requests
import json

class OAuth2ClientCredentialsOperation(Asserter):
    KEY_CLIENT_ID = "client_id"
    KEY_CLIENT_SECRET = "client_secret"
    KEY_GRANT_TYPE = "grant_type"
    KEY_AUDIENCE = "audience"
    PATH_OAUTH = "oauth"
    PATH_TOKEN = "token"

    def __init__(self, baseurl, clientId, clientSecret):
        self.baseUrl = baseurl
        self.clientId = clientId
        self.clientSecret = clientSecret
    
    def getAccessToken(self, baseurl):
        self.assertNotNull(self.baseUrl, "Service")
        audience = self.baseUrl
        if (not audience.startswith("https://") or audience.startswith("http://")):
            audience = "https://" + audience
        # url = audience + "/" + self.PATH_OAUTH + "/" + self.PATH_TOKEN
        request = {
            self.KEY_CLIENT_ID : self.clientId,
            self.KEY_CLIENT_SECRET: self.clientSecret,
            self.KEY_GRANT_TYPE :GrantType.CLIENT_CREDENTIALS,
            "audience": baseurl
            }
        payload = json.dumps(request)
        headers = {HttpHeader().CONTENT_TYPE : MediaType().APPLICATION_JSON, HttpHeader().ACCEPT : MediaType().APPLICATION_JSON}
        response = requests.post("https://auth.reloadly.com/oauth/token", data=payload, headers=headers)
        response_data = response.json()
        access_token = response_data["access_token"]
        return access_token
