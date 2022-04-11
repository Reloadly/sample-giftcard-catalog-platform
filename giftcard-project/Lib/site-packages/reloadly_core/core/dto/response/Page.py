import json


class Page(object):
    def __init__(self, content : list, number : int, size : int, totalElements : float, pageable : json.JSONEncoder , last : bool, totalPages : int, sort : json.JSONEncoder, first : bool, numberOfElements : int):
        self.content = content
        self.number = number
        self.size = size
        self.totalElements = totalElements
        self.pageable = pageable
        self.last = last
        self.totalPages = totalPages
        self.sort = sort
        self.first = first
        self.numberOfElements = numberOfElements
        super(Page, self).__init__(content, number, size, totalElements, pageable, last, totalPages, sort, first, numberOfElements)

    def Page(self, content : list, pageable, total : int):
        return content, pageable, total

    def Page(self, content : list):
        return content
