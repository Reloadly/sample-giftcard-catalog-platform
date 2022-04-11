from reloadly_core.core.exception.ReloadlyException import ReloadlyException
import datetime
"""
 * Class that represents an Reloadly Server error captured from a http response. Provides different methods to get a clue of why the request failed.
 * i.e.:
 * <pre>
 * {@code
 * {
 *      "details": [],
 *      "errorCode": null
 *      "httpStatusCode": 400,
 *      "message": "Invalid operator id provided",
 *      "path": "/operators/68695596",
 *      "timeStamp": 1559108814252,
 * }
 * }
 * </pre>
"""
class APIException(ReloadlyException):

    def __init__(self):
        #Additional details that might be helpful in understanding the error(s) that occurred.
        self.details = []

        #For some errors that could be handled programmatically, a string summarizing the error reported.
        self.errorCode = ""

        """"
        * HTTP status indicate whether a specific HTTP request has been successfully completed.
        * Responses are grouped in five classes: informational responses, successful responses,
        * redirects, client errors, and servers errors.
        * See <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html">https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html</a>
        """
        self.httpStatusCode = 0

        #The end-point that was used when the error occurred
        self.path = ""

        #The timestamp when the usage occurred
        self.timeStamp = datetime()

    def APIException(self, message):
        super(message)

    def APIException(self, message, httpStatusCode, path):
        super(message)
        self.path = path
        self.httpStatusCode = httpStatusCode
        self.timeStamp = datetime.time()

    def APIException(self, message, httpStatusCode, path, errorCode):
        super(message)
        self.path = path
        self.httpStatusCode = httpStatusCode
        self.timeStamp = datetime.time()
        self.errorCode = errorCode

    def APIException(self, message, httpStatusCode, path, errorCode, details):
        super(message)
        self.path = path
        self.httpStatusCode = httpStatusCode
        self.timeStamp = datetime.time()
        self.errorCode = errorCode
        self.details = details
