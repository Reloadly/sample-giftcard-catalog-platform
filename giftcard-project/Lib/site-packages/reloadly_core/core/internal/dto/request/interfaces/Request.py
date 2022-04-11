import reloadly_core.core.exception.APIException as APIException
import reloadly_core.core.exception.ReloadlyException as ReloadlyException
from abc import ABC, abstractmethod

class Request(ABC):
    @abstractmethod
    def __init__(self):
        raise ReloadlyException


