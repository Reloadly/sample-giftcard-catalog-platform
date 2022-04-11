from urllib3 import PoolManager
from mock import Mock
from reloadly_giftcard.giftcard.tests.util.RecordedRequestMatcher import RecordedRequestMatcher
from reloadly_core.core.enums.Environment import Environment
import os
import json
from dotenv import load_dotenv

load_dotenv('.env')

class GiftCardAPIMockServer():
    accessToken = os.environ.get('GIFTCARD_ACCESS_TOKEN')
    clientId = os.environ.get('CLIENT_ID')
    clientSecret = os.environ.get('CLIENT_SECRET')
    environment = Environment.GIFTCARD_SANDBOX
    def __init__(self):
        self.server = Mock()

    def stop(self):
        self.server = None

    def getBaseUrl(self):
        url = str(self.server.url)
        return url.replace("/\\z", "")

    def takeRequest(self):
        return self.server.RecordedRequestMatcher()

    def readTextFile(self, path):
        f = open( path , "r")
        a = f.read()
        return a

    def jsonResponse(self, path, statusCode):
        with open(path,'r') as f:
            data = json.load(f)
            return data
            