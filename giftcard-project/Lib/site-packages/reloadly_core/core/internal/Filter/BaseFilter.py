from abc import ABC

class BaseFilter(ABC):
    def __init__(self):
        self.parameters = {}
