class country:
    def __init__(self, Country):
        #ISO 3166-1 alpha-2 Country code. See https://www.iso.org/obp/ui/#search
        self.isoName = Country['isoName']
        #Full country name
        self.name = Country['name']
        #Account ISO-4217 3 letter currency code for the given country.
        #See https://www.iso.org/iso-4217-currency-codes.html
        self.currencyCode = Country['currencyCode']
        #Full currency name
        self.currencyName = Country['currencyName']
        #Symbol of currency
        self.currencySymbol = Country['currencySymbol']
        #Url of country flag image
        self.flag = Country['flag']
        #Calling codes of the country
        self.callingCodes = Country['callingCodes']


    
