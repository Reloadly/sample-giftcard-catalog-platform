import json
import datetime

class JackSonDateDeserializer(json):
    def deserialize(self, jsonParser):
        try:
            a = datetime(jsonParser.dumps())
            return a.strftime("%Y/%m/%d %H:%M:%S")
        except:
            raise RuntimeError()

