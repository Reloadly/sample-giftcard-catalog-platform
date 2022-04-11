from reloadly_core.core.exception.APIException import APIException
""""
 * Represents a server error when a rate limit has been exceeded.
 * <p>
 * Getters for {@code limit, remaining} and {@code reset} corresponds to {@code X-RateLimit-Limit, X-RateLimit-Remaining} and {@code X-RateLimit-Reset} HTTP headers.
 * If the value of any headers is missing, then a default value -1 will assigned.
 * <p>
 * To learn more about rate limits, visit <a href="https://api.reloadly.com/docs/policies/rate-limits">https://api.reloadly.com/docs/policies/rate-limits</a>
"""

class RateLimitException(APIException):
    def __init__(self):
        self.limit = 0
        self.remaining = 0
        self.expectedResetTimestamp = 0
        self.STATUS_CODE_TOO_MANY_REQUEST =429

    def RateLimitException(self, message, httpStautsCode, path, errorCode):
        return message,httpStautsCode,path, errorCode

    def RateLimitException(self, message, httpStautsCode, path, errorCode, details):
        return message,httpStautsCode,path, errorCode,details
    
    def getLimit(self):
        return self.limit

    def setLimit(self, limit):
        self.limit = limit

    def getRemaining(self):
        return self.remaining

    def setRemaining(self, remaining):
        self.remaining = remaining


    def getExpectedResetTimestamp(self):
        return self.expectedResetTimeStamp

    def setExpectedResetTimestamp(self, expectedResetTimeStamp : int):
        self.expectedResetTimeStamp = expectedResetTimeStamp

    


