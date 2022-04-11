import reloadly_core.core.dto.APIError as APIError
import reloadly_core.core.exception.APIException as APIException
import reloadly_core.core.exception.RateLimitException as RateLimitException
import reloadly_core.core.exception.ReloadlyException as ReloadlyException
import reloadly_core.core.internal.util.ExceptionUtil as ExceptionUtil
from reloadly_core.core.internal.dto.request.BaseRequest import BaseRequest
from reloadly_core.core.internal.dto.request.CustomizableRequest import CustomizableRequest
from reloadly_core.core.internal.constant.MediaType import MediaType
import json
import os
import datetime
from requests import *
from urllib.parse import urljoin

class CustomRequest(BaseRequest, CustomizableRequest):


    def __init__(self, url : str, method : str):
        self.url = url
        self.method = method
        self.mapper = {}
        self.Type = ""
        self.headers = {}
        self.parameters = {}
        self._STATUS_CODE_TOO_MANY_REQUEST = 429

    def CustomRequest(self, url : str, method : str):
        super().__init__(url, method)

    def createRequest(self):
        builder = Request.Builder().url(self.url).method(self.method, self.createBody())
        self.addHeader(builder)
        return builder.build() 

    def addHeader(self, name : str, value : str):
        self.header[name] = value
        return self
    
    def addParameter(self, name : str, value : str):
        self.parameters[name] =  value
        return self

    def setBody(self, value : str):
        self.body = value

    def createBody(self):
        if (self.body==None and self.parameters):
            return None

        try:
            jsonBody = {self.mapper, self.parameters}
            return self.body.append(MediaType.parse("APPLICATION_JSON"), jsonBody) # confirm if the parsing works
        
        except:
            raise ReloadlyException("Couldn't create the request body")

    def createResponseException(self, response):
        if response.code() == self._STATUS_CODE_TOO_MANY_REQUEST:
            return self.createRateLimitException(response)

        try:
            body = response.body()
            if not body:
                raise Exception("Operation failed")
            
            streamReader = os.read(body, 12)
            return ExceptionUtil.convert(json.dumps(streamReader),response.code())
        except:
            return APIException(str(body), response.code(), self.getPath(response))

    def createRateLimitException(self, response):
        rateLimitException = self.createResponseException(response)
        resetValue = response.header("X-RateLimit-Reset", "-1")
        limitValue = response.header("X-RateLimit-Limit", "-1")
        remainingValue = response.header("X-RateLimit-Remaining", "-1")

        limit = int(limitValue)
        remaining = int(remainingValue)
        reset = int(resetValue)

        rateLimitException.setLimit(limit)
        rateLimitException.setRemaining(remaining)
        rateLimitException.setExpectedResetTimestamp(reset)
        return rateLimitException

    def getPath(self, response):
        return urljoin(response.request().url().pathsegments(), "/")