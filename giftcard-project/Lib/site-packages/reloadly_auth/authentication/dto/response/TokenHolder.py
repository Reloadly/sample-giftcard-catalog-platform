import reloadly_auth.authentication.client.AuthenticationAPI as AuthenticationAPI

#Class that contains the Tokens obtained after a call to the {@link AuthenticationAPI} methods.
class TokenHolder:
    def __init__(self):
        self.accessToken = ""
        self.tokenType = ""
        self.expiresIn = 0.0


    def getToken(self):
        return self.accessToken

    def getTokenType(self,):
        return self.tokentype

    def getExpiresIn(self):
        return self.expiresIn
