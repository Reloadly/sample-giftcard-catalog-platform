import reloadly_core.core.internal.net.Telemetry as Telemetry


class TelemetryInterceptor():
    def __init__(self):
        self.enabled = True
        self.telemetry = Telemetry()

    def TelemetryInterceptor(self, telemetry : Telemetry):
        self.telemetry = telemetry
        self.enabled = True

    #def intercept(self, chain)

