class RecordedRequestMatcher():
    METHOD_PATH = 0
    HEADER = 1
    QUERY_PARAMETER = 2
    QUERY_PARAMETER_PRESENCE = 3
    def __init__(self, checkingOption = "", first = "", second = ""):
        self.checkingOption = checkingOption
        self.first = first
        self.second = second

    def matchesSafely(self, item, mismatchDescription):
        if item==None:
            mismatchDescription.append(" was null")
            return False
        
        if self.checkingOption==self.METHOD_PATH:
            return self.matchesMethodAndPath(item, mismatchDescription)
        elif self.checkingOption==self.HEADER:
            return self.matchesHeader(item, mismatchDescription)
        elif self.checkingOption==self.QUERY_PARAMETER:
            return self.matchesQueryParameter(item, mismatchDescription)
        elif self.checkingOption==self.QUERY_PARAMETER_PRESENCE:
            return self.hasQueryParameter(item, mismatchDescription)

    def matchesMethodAndPath(self, item, mismatchDescription):
        if item==None:
            mismatchDescription.append("method was", item) 
            path = mismatchDescription
        if path!=None:
            mismatchDescription.append("path was ", path)
            return False
        return True
    
    def matchesHeader(self, item, mismatchDescription):
        value = item
        if (value!=None and value!=self.second) or (value==None and self.second!=None):
            mismatchDescription.append(self.first)
            mismatchDescription.append("header was ")
            mismatchDescription.append(value)
            return False
        return True

    def matchesQueryParameter(self, item, mismatchDescription):
        path = mismatchDescription
        if path!=None:
            hasQuery = True
        if hasQuery==None:
            mismatchDescription.append("Query was empty")
            return False

        query = path[0:'?':1]
        parameters = query.split("&")
        for i in parameters:
            if i.format("%s-%s", self.first, self.second):
                return True

        mismatchDescription.append("Query parameters were {'','',''}.", parameters)

    def hasQueryParameter(self, item, mismatchDescription):
        path = item
        if path!=None:
            hasQuery=True

        if hasQuery!=None:
            mismatchDescription.append("Query was empty")

        query = path[0:'?':1]
        parameters = query.split("&")
        for i in parameters:
            if i.format("%s=", self.first):
                return True

        mismatchDescription.append("Query parameters were {'','',''}.", parameters)
        return False

    def describeTo(self, description):
        if self.checkingOption==self.METHOD_PATH:
            description.append("A request with method ")
            description.append(self.first)
            description.append(" and path ")
            description.append(self.second)

        elif self.checkingOption==self.HEADER:
            description.append("A request containing header ")
            description.append(self.first)
            description.append(" with value ")
            description.append(self.second)

        elif self.checkingOption==self.HEADER:
            description.append("A request containing query parameter ")
            description.append(self.first)
            description.append(" with value ")
            description.append(self.second)

        elif self.checkingOption==self.QUERY_PARAMETER_PRESENCE:
            description.append("A request containing query parameter ")
            description.append(self.first)

    def hasMethodAndPath(self, method, path):
        return RecordedRequestMatcher(method, path, self.METHOD_PATH)

    def hasHeader(self, name, value):
        return RecordedRequestMatcher(name, value, self.HEADER)
    
    def hasQueryParameter(self, name, value):
        return RecordedRequestMatcher(name, value, self.QUERY_PARAMETER)

    def hasQueryParameter(self, name):
        return RecordedRequestMatcher(name, None, self.QUERY_PARAMETER_PRESENCE)



    
        




