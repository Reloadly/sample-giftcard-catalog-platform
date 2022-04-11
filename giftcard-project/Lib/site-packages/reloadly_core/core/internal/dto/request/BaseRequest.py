from reloadly_core.core.internal.dto.request.interfaces.Request import Request
import reloadly_core.core.exception.ReloadlyException as ReloadlyException
from requests import Request
class BaseRequest(Request):
    def __init__(self, client):
        self.client = client

    def execute(self):
        request = Request()
        try:
            r = request.prepare()
            s = request.Session()
            s.send(r)

            #response = client.newCall(request).execute()
            #return ParseResponse(response)
        except:
            raise ReloadlyException("Failed to execute request")





