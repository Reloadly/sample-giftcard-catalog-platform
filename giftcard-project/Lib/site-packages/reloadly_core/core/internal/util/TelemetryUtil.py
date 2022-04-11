import reloadly_core.core.internal.interceptor.TelemetryInterceptor as TelemetryInterceptor
import reloadly_core.core.internal.net.Telemetry as Telemetry
import reloadly_core.core.internal.util.Asserter as Asserter
import sys

class TelemetryUtil:

    def getTelemetryInterceptor(self, libraryVersion : str, apiVersion : str):
        name = "reloadly_sdk_python"
        Asserter.assertNotBlank(libraryVersion, "Library Version")
        if apiVersion:
            return TelemetryInterceptor(Telemetry(name, libraryVersion, apiVersion))

        return TelemetryInterceptor(Telemetry(name, libraryVersion))
