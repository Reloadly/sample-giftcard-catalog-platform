import reloadly_auth.authentication.dto.response.TokenHolder as TokenHolder
import reloadly_core.core.internal.dto.request.interfaces.Request as Request
from abc import ABC, abstractmethod

#Class that represents an OAuth 2.0 Authentication/Authorization request. The execution will return a {@link TokenHolder}.
class OAuth2ClientCredentialsRequest(ABC):
    @abstractmethod
    def setAudience(self,audience : str):
        pass
