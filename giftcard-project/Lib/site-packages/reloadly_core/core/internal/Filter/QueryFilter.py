from reloadly_core.core.internal.util.Asserter import Asserter
from reloadly_core.core.internal.Filter.BaseFilter import BaseFilter

class QueryFilter(BaseFilter):
    """Filter by page
     *
     * @param pageNumber the page number to retrieve.
     * @param pageSize   the amount of items per page to retrieve.
     * @return this filter instance"""

    INCLUDE_PIN = "includePin"
    INCLUDE_DATA = "includeData"
    INCLUDE_BUNDLES = "includeBundles"
    INCLUDE_SUGGESTED_AMOUNTS = "suggestedAmounts"
    INCLUDE_RANGE_DENOMINATION_TYPE = "includeRange"
    INCLUDE_FIXED_DENOMINATION_TYPE = "includeFixed"
    INCLUDE_SUGGESTED_AMOUNTS_MAP = "suggestedAmountsMap"
    PAGE = "page"
    PAGE_SIZE = "size"

    def withPage(self, pageNumber : int, pageSize : int):
        Asserter().assertNotNull(pageNumber, "Page number")
        Asserter().assertNotNull(pageSize, "Page size")
        if pageNumber<=0:
            raise Exception("Filter page number must be greater than zero")
        if pageSize<=0:
            raise Exception("Filter page size must be greater than zero")
        else:
            self.parameters["page"] = pageNumber
            self.parameters["size"] = pageSize
            return self.parameters



