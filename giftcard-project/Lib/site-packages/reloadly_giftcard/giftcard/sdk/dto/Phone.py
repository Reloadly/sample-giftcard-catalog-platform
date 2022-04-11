class Phone:
    def __init__(self, number, countryCode):
        #Phone number
        self.number = number
        #ISO 3166-1 alpha-2 Country code. See https://www.iso.org/obp/ui/#search
        self.CountryCode = countryCode
