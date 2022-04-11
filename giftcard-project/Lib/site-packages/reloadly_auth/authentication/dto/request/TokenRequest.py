from reloadly_auth.authentication.dto.request.OAuth2ClientCredentialsRequest import OAuth2ClientCredentialsRequest
from reloadly_core.core.internal.dto.request.CustomRequest import CustomRequest

class TokenRequest(CustomRequest):
    def __init__(self, url : str):
        super().__init__(url, "POST")
        
    def set_audience(self, audience : str):
        super().addParameter(audience, "audience")
        return self

        
