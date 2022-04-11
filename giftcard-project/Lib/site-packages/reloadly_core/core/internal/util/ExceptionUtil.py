import reloadly_core.core.dto.APIError as APIError
import reloadly_core.core.exception.APIException as APIException
import reloadly_core.core.exception.OAuthException as OAuthException

class ExceptionUtil:
    def __init__(self) -> None:
        pass
    
    def isAuthenticationError(apiError : APIError):
        if not apiError.getPath():
            return

    def doGetApiException(self, apiError : APIError, httpStatusCode : int):
        if self.isAuthenticationError(apiError):
            return OAuthException(apiError.getMessage, httpStatusCode, apiError.getPath())
        return APIException(apiError.getMessage(), httpStatusCode, apiError.getPath())


    def doGetApiException(self, apiError : APIError, httpStatusCode : int, cause):
        if self.isAuthenticationError(apiError):
            return OAuthException(apiError.getMessage, httpStatusCode, apiError.getPath(), cause)
        return APIException(apiError.getMessage(), httpStatusCode, apiError.getPath(), cause)

    def setAdditionalFields(apiError : APIError, apiException : APIException):
        if apiError.getTimeStamp():
            apiException.setTimeStamp(apiError.geTimeStamp())
        if apiError.getDetails():
            apiException.setDetails(apiError.getDetails())
            return apiException
    
    def convert(self, apiError : APIError, httpStatusCode : int):
        return self.setAdditionalFields(apiError, self.doGetApiException(apiError, httpStatusCode))

    def convert(self, apiError : APIError, httpStatusCode : int, cause):
        return self.setAdditionalFields(apiError, self.doGetApiException(apiError, httpStatusCode, cause))
    
    

