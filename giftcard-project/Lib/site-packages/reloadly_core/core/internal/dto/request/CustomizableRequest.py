from reloadly_core.core.internal.dto.request.interfaces.Request import Request

class CustomizableRequest(Request):
    def __init__(self):
        self.name = ""
        self.value = ""
        

    def addHeader(self, name, value):
        self.header[name] = value
        return self
