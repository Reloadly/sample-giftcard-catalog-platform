from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter
from reloadly_core.core.internal.util.Asserter import Asserter
import datetime as datetime



class TransactionHistoryFilter(QueryFilter):
    END_DATE = "endDate"
    START_DATE = "startDate"
    OPERATOR_ID = "operatorId"
    COUNTRY_CODE = "countryCode"
    OPERATOR_NAME = "operatorName"
    CUSTOM_IDENTIFIER = "customIdentifier"

    def getParameters(self):
        self.parameters = {}
        return self

    def withPage(self, pageNumber : int, pageSize : int):
        super().withPage(pageNumber,pageSize)
        return self.parameters

    """@param operatorId - Operator id to filter by
     * @return - TransactionHistoryFilter"""
    def operatorId(self, operatorId : int):
        Asserter().assertNotNull(operatorId, "Operator id")
        Asserter().assertGreaterThanZero(operatorId,"Operator id")
        self.parameters[self.OPERATOR_ID] = operatorId
        return self.parameters

    """ @param countryCode - Country code to filter by
     * @return - TransactionHistoryFilter"""
    def CountryCode(self, CountryCode):
        Asserter().assertNotNull(self.countryCode, "Country Code")
        self.parameters[self.COUNTRY_CODE] = self.countryCode.getAlpha2()
        return self.parameters

    """@param operatorName - Operator name to filter by
     * @return - TransactionHistoryFilter"""
    def operatorName(self, operatorName : str):
        Asserter().assertNotBlank(operatorName, "Operator name")
        self.parameters[self.OPERATOR_NAME] = operatorName
        return self.parameters
    

    """@param customIdentifier - Custom identifier to filter by
     * @return - TransactionHistoryFilter"""
    def customIdentifier(self, customIdentifier : str):
        Asserter().assertNotBlank(customIdentifier, "Custom identifier")
        self.parameters[self.CUSTOM_IDENTIFIER] = customIdentifier
        return self.parameters

    """@param startDate - Date range start date to filter by
     * @return - TransactionHistoryFilter"""
    def startDate(self, startDate = datetime.datetime.now()):
        Asserter().assertNotNull(startDate, "Start date")
        self.parameters[self.START_DATE] = startDate.strftime("%m/%d/%Y, %H:%M:%S")
        return self.parameters
    
    """@param endDate - Date range end date to filter by
     * @return - TransactionHistoryFilter"""
    def endDate(self, endDate = datetime.datetime.now()):
        Asserter().assertNotNull(endDate, "End date")
        self.parameters[self.END_DATE] = endDate.strftime("%m/%d/%Y, %H:%M:%S")
        return self.parameters

        

    



    
         



