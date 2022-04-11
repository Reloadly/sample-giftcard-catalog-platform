from reloadly_core.core.net.ProxyOptions import ProxyOptions

#Used to configure additional configuration options when customizing the API client instance.
 
class HttpOptions:
    def __init__(self):
        self.proxyOptions = ProxyOptions()
        self.readTimeout = 180
        self.writeTimeout = 180
        self.connectTimeout = 180

    def HttpOptions(self, readTimeout, writeTimeout, connectTimeout, proxyOptions):
        self.readTimeout = readTimeout
        self.writeTimeout = writeTimeout
        self.connectTimeout = connectTimeout
        self.proxyOptions = ProxyOptions()

    
        


