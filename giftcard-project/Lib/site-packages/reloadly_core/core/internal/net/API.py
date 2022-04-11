import reloadly_core.core.internal.interceptor.TelemetryInterceptor as TelemetryInterceptor
import reloadly_core.core.internal.util.TelemetryUtil as TelemetryUtil
import reloadly_core.core.net.HttpOptions as HttpOptions
import reloadly_core.core.net.ProxyOptions as ProxyOptions
import reloadly_core.core.internal.constant.HttpHeader as HttpHeader
from reloadly_core.core.internal.enums.Version import Version
from abc import ABC, abstractmethod
import requests

class API(ABC):
    KEY_CLIENT_ID = "client_id"
    KEY_CLIENT_SECRET = "client_secret"
    def __init__(self):
        self.libraryVersion = ""

    def API(self, clientId : str, clientSecret : str, enableLogging : bool, redactHeaders : list, options ,enableTelemetry : bool):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.enableLogging = enableLogging
        self.libraryVersion = Version.LIBRARY_VERSION
        if (redactHeaders!=None and len(redactHeaders)!=0):
            self.headersToRedact = []
        if enableTelemetry==None:
            self.enableTelemetry = True

        options = HttpOptions()
        client = self.buildClient(options)

    def API(self, clientId : str, clientSecret : str, enableLogging : bool, redactHeaders : list, options, enableTelemetry : bool):
        self.client_id = clientId
        self.clientSecret = clientSecret
        self.enableLogging = enableLogging
        if len(redactHeaders)>0:
            self.headersToRedact = []
        self.enableTelemetry = enableTelemetry
        if options == None:
            options = HttpOptions()
            client = self.buildClient(options)

    def isLoggingEnabled(self):
        return self.enableLogging

    def createUrlFromString(self, url : str):
        try:
            return url
        except:
            return ""

    def buildClient(self, options):
        if not options.readTimeout:
            readTimeout = 60
            writeTimeout = 60
            connectTimeout = 60
        else:
            readTimeout = options.readTimeout
            writeTimeout = options.writeTimeout
            connectTimeout = options.connectTimeout

        proxyOptions = options.proxyOptions() # formely proxyOptions
        clientBuilder = requests.Request()
        if proxyOptions:
            proxy = proxyOptions.proxy
            proxyAuth = proxyOptions.BasicAuthentication
            if proxyAuth:
                requests.HTTPProxyAuth(self.client_id, self.clientSecret)
                if clientBuilder.header[HttpHeader.PROXY_AUTHORIZATION_HEADER]:
                    return None
                return clientBuilder.header[HttpHeader.PROXY_AUTHORIZATION_HEADER]
        builder = clientBuilder.connectTimeout(connectTimeout).readTimeout(readTimeout).writeTimeout(writeTimeout)
        if self.enableLogging:
            #httpLoggingInterceptor = HttpLoggingInterceptor()
            #httpLoggingInterceptor.setLevel(Level.BODY)
            if self.headersToRedact!=None:
                for i in self.headersToRedact:
                    if i.strip()!=False:
                        self.redactHeader.append(i.strip())

            #builder.addInterceptor(httpLoggingInterceptor)
        if self.enableTelemetry:
            telemetryInterceptor = TelemetryUtil.getTelemetryInterceptor(Version.LIBRARY_VERSION, Version.API_VERSION)
            telemetryInterceptor.setEnabled(True)
            builder.addInterceptor.setEnabled(True)
            builder.addInterceptor(telemetryInterceptor)
        return builder.build()
