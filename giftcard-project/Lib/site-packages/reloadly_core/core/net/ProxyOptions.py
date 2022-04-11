import reloadly_core.core.internal.util.Asserter as Asserter
from urllib3 import ProxyManager, make_headers

#Used to configure Proxy-related configurations.
class ProxyOptions:
    def __init__(self, proxyHost = "", proxyUsername = "", proxyPassword = "", basicAuthentication = "", proxyPort = 8080):
        self.proxyHost = proxyHost
        self.proxyUsername = proxyUsername
        self.proxyPassword = proxyPassword
        self.basicAuthentication = basicAuthentication
        self.proxyPort = proxyPort
    """Builds a new instance using the given Proxy.
     * The Proxy will not have authentication unless {@link #basicAuthentication} is set.
     *
     * @param proxy - The proxy setting"""
    def ProxyOperations(self):
        Asserter.assertNotNull(self.proxyHost, "Proxy")
        
    def ProxyOperations(self, proxyHost , proxyUsername , proxyPassword):
        Asserter.assertNotNull(proxyHost, "Proxy")
        self.validateAndBuildAuthenticationCredentials()
        #Validate and build the authentication value to use for this Proxy.
        
    def validateAndBuildAuthenticationCredentials(self):
        if self.proxyUsername:
            Asserter.assertNotBlank(self.proxyUsername, "Proxy username")
            Asserter.assertNotNull(self.proxyPassword, "Proxy password")
            default_headers = make_headers(proxy_basic_auth= self.proxyUsername + ":" + self.proxyPassword)
            http = ProxyManager(self.url + ":" + self.proxyPort + "/", proxy_headers=default_headers)

