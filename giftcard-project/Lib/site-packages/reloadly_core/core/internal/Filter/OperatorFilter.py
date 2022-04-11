from reloadly_core.core.internal.Filter.QueryFilter import QueryFilter

#Class used to filter the results received when calling the Operators endpoint.
#Related to the {@link OperatorOperations}.

class OperatorFilter(QueryFilter):
    INCLUDE_PIN = "includePin"
    INCLUDE_DATA = "includeData"
    INCLUDE_BUNDLES = "includeBundles"
    INCLUDE_SUGGESTED_AMOUNTS = "suggestedAmounts"
    INCLUDE_RANGE_DENOMINATION_TYPE = "includeRange"
    INCLUDE_FIXED_DENOMINATION_TYPE = "includeFixed"
    INCLUDE_SUGGESTED_AMOUNTS_MAP = "suggestedAmountsMap"
    
    def __init__(self):
        self.parameters = {
            self.INCLUDE_PIN : True,
            self.INCLUDE_DATA : True,
            self.INCLUDE_BUNDLES : True,
            self.INCLUDE_SUGGESTED_AMOUNTS : False,
            self.INCLUDE_SUGGESTED_AMOUNTS_MAP : False,
            self.INCLUDE_RANGE_DENOMINATION_TYPE : True,
            self.INCLUDE_FIXED_DENOMINATION_TYPE : True,
            }

    def getParameters(self):
        self.parameters = {
            self.INCLUDE_PIN : True,
            self.INCLUDE_DATA : True,
            self.INCLUDE_BUNDLES : True,
            self.INCLUDE_SUGGESTED_AMOUNTS : False,
            self.INCLUDE_SUGGESTED_AMOUNTS_MAP : False,
            self.INCLUDE_RANGE_DENOMINATION_TYPE : True,
            self.INCLUDE_FIXED_DENOMINATION_TYPE : True,
            }
        

    def withPage(self, pageNumber : int, pageSize : int):
        super().withPage(pageNumber, pageSize)
        return self

        #Whether to include pin-based operators in response
        #@param includePin - Whether to include pin-based operators in response
        #@return - OperatorFilter
    def includePin(self, includePin : bool):
        self.parameters[self.INCLUDE_PIN] = includePin
        return self

        #@param includePin - Whether to include pin-based operators in response
        #@return - OperatorFilter
    def includeData(self, includeData : bool):
        self.parameters[self.INCLUDE_DATA] = includeData
        return self
        
        """Whether to include bundles operators in response
        @param includeBundles - Whether to include bundles in response
        @return - OperatorFilter"""
    def includeBundles(self, includeBundles : bool):
        self.parameters[self.INCLUDE_BUNDLES] = includeBundles
        return self

        """Whether to include suggestedAmount field in response
            @param includeSuggestedAmounts - Whether to include suggested amounts in response
            @return - OperatorFilter"""
    def includeSuggestedAmounts(self, includeSuggestedAmounts : bool):
        self.parameters[self.INCLUDE_SUGGESTED_AMOUNTS] = includeSuggestedAmounts
        return self
        
        """Whether to include suggestedAmountsMap field in response
        @param includeSuggestedAmountsMap - Whether to include suggested amounts map in response
        @return - OperatorFilter"""
    def includeSuggestedAmountsMap(self, includeSuggestedAmountsMap : bool):
        self.parameters[self.INCLUDE_SUGGESTED_AMOUNTS_MAP] = includeSuggestedAmountsMap
        return self

        """Whether to include operators where denomination type is RANGE in response
        @param includeRangeDenominationType - Whether to include range denomination type
        @return - OperatorFilter"""
    def includeRangeDenominationType(self, includeRangeDenominationType : bool):
        self.parameters[self.INCLUDE_RANGE_DENOMINATION_TYPE] = includeRangeDenominationType
        return self

        """Whether to include operators where denomination type is FIXED in response
        @param includeFixedDenominationType - Whether to include fixed denomination type
        @return - OperatorFilter"""
    def includeFixedDenominationType(self, includeFixedDenominationType : bool):
        self.parameters[self.INCLUDE_FIXED_DENOMINATION_TYPE] = includeFixedDenominationType
        return self
        