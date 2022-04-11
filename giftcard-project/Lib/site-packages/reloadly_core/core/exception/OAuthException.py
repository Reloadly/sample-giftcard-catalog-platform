from reloadly_core.core.exception.APIException import APIException

class OAuthException(APIException):

    def OAuthException(self, message):
        return message

    def OAuthException(self, message, httpStatusCode, path):
        return message, httpStatusCode, path

    def OAuthException(self, message, cause, path, errorCode):
        return message, cause, path, errorCode

    def OAuthException(self, message, cause, path, errorCode, details):
        return message, cause, path, errorCode, details
    
    def OAuthException(self, message, path, httpStatusCode, cause):
        return message, path, httpStatusCode, cause

    def OAuthException(self, message, path, httpStatusCode, errorCode, details, cause):
        return message, path, httpStatusCode, errorCode, details, cause

    def OAuthException(self, message, cause):
        return message, cause

    def OAuthException(self, message, cause,httpStatusCode, errorCode, details):
        return message, cause,httpStatusCode, errorCode, details

    # def getErrorCode(self):
    #     pass

    def isExpiredToken(self):
        if not self.getErrorCode():
            return True