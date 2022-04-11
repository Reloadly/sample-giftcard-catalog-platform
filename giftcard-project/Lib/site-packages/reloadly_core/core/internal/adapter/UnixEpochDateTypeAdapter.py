import json
import datetime

class UnixEpochDateTypeAdapter(json):
    def write(self, out : str, value : datetime()):
        if value==None:
            out = None
        else:
            out = json.loads(value)

    def read(self, In : datetime):
        if not In:
            return None
        else:
            return datetime(In)
            

        

