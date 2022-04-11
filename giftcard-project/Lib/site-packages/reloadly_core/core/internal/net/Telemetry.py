from opentelemetry.launcher import configure_opentelemetry
import json

class Telemetry():
    ENV_KEY = "env"
    PYTHON_KEY = "python"
    NAME_KEY = "name"
    VERSION_KEY = "api-version"
    HEADER_NAME = "Reloadly-client"
    LIBRARY_VERSION_KEY = "reloadly-sdk_python"
    def __init__(self):
        self.name = ""
        self.value = ""
        self.env = {}
    def configure_Telemetry(self, name = "Reloadly", libraryVersion = ""):
        configure_opentelemetry(
            access_token = self.accessToken,
            service_name = name,
            resource_attributes = {
                "host.hostname" : self.client
            }

        )
        self.name = name
        self.libraryVersion = libraryVersion

    def Telemetry(self, name : str, libraryVersion : str, apiVersion : str):
        self.name = name
        self.apiVersion = apiVersion
        self.libraryVersion = libraryVersion
        if not name:
            self.env = {}
            self.value = ""
            return 

        values = {}
        values[self.NAME_KEY] = name
        if not apiVersion:
            values[self.VERSION_KEY] = apiVersion
        tmpEnv = {}
        if not libraryVersion:
            tmpEnv[self.LIBRARY_VERSION_KEY] = libraryVersion
        self.env.update(tmpEnv)
        values[self.ENV_KEY] = self.env
        tmpValue = ""
        try:
            mapper = json.dumps(values)
        except:
            tmpValue = None

        self.value = tmpValue

    #def latency_parameter(self):



