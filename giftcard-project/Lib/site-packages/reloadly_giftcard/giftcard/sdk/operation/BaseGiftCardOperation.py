from reloadly_core.core.internal.client.BaseOperation import BaseOperation
from reloadly_core.core.internal.constant.HttpHeader import HttpHeader
from reloadly_core.core.internal.constant.MediaType import MediaType
from reloadly_core.core.internal.dto.request.CustomRequest import CustomRequest
from reloadly_core.core.internal.dto.request.interfaces.Request import Request
from reloadly_core.core.internal.enums.Version import Version
from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.Filter.OperatorFilter import OperatorFilter
import requests, json, urllib
import time


class BaseGiftCardOperation(BaseOperation):
    def __init__(self, client, baseUrl, apiToken):
        self.client = client
        self.baseUrl = baseUrl
        self.apiToken = apiToken
        super().__init__(client, baseUrl, apiToken)

    def buildFilters(self, Filter, endPoint : str):
        self.baseUrl = self.baseUrl + "/" + endPoint
        if Filter:
            para  = Filter.getParameters()
            if type(para)==dict:
                for key in para:
                    self.baseUrl = self.getBuilder(para[key])
        return self.baseUrl

    def buildQueryFilters(self, Filter, endPoint : str):
        self.baseUrl = self.baseUrl + "/" + endPoint
        if Filter:
            self.baseUrl = self.baseUrl + "?" + self.queryBuilder(Filter)
        return self.baseUrl

    def createGetRequest(self, baseUrl):
        a = self.startTime()
        headers = {HttpHeader.ACCEPT : Version().GIFTCARD_V1, HttpHeader.AUTHORIZATION: "Bearer " + self.apiToken}
        r = requests.get(baseUrl, headers = headers)
        b = r.json()
        self.requestLatency = self.requestlatency(a)
        if "errorCode" in b:
            raise Exception(b["message"])
        return b
        

    def createPostRequest(self, url : str, body):
        a = self.startTime()
        headers = {HttpHeader.ACCEPT : Version.GIFTCARD_V1, HttpHeader.CONTENT_TYPE : MediaType.APPLICATION_JSON, HttpHeader.AUTHORIZATION: "Bearer " + self.apiToken}
        encoded_data = json.dumps(body).encode('utf-8')
        p = requests.post(url, headers = headers, data = encoded_data)
        b = p.json()
        self.requestLatency = self.requestlatency(a)
        if "errorCode" in b:
            raise Exception(b["message"])
        return b

    def getBuilder(self, endPoint : str):
        return self.baseUrl + "/" + endPoint

    def startTime(self):
        return time.time()

    def requestlatency(self, a):
        return time.time() - a
    
    def queryBuilder(self, Filter):
        return urllib.parse.urlencode(Filter)