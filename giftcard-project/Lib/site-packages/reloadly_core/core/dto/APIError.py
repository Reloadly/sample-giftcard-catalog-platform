"""
* Class that represents an Reloadly Server error captured from a http response. Provides different methods to get a clue of why the request failed.
 * i.e.:
 * <pre>
 * {@code
 * {
 *      "details": [],
 *      "errorCode": null
 *      "message": "Invalid operator id provided",
 *      "path": "/operators/68695596",
 *      "timeStamp": 1559108814252,
 * }
 * }
 * </pre>
"""
import datetime


class APIError:
    def __init__(self):
        self.details = []
        self.errorCode = ""
        self.infoLink = ""
        self.message = ""
        self.path = ()
        self.timeStamp = datetime()

    def APIError(self, message, path, timeStamp):
        self.message = message
        self.path = path
        self.timeStamp = timeStamp


    def APIError(self, message, path, timeStamp, errorCode):
        self.message = message
        self.path = path
        self.timeStamp = timeStamp
        self.errorCode = errorCode

    def APIError(self, message, path, timeStamp, errorCode, details):
        self.message = message
        self.path = path
        self.timeStamp = timeStamp
        self.errorCode = errorCode
        self.details = details

    def APIError(self, message, path, timeStamp, errorCode, details , infoLink):
        self.message = message
        self.path = path
        self.timeStamp = timeStamp
        self.errorCode = errorCode
        self.details = details
        self.infoLink = infoLink

