from abc import ABC, abstractmethod


class Seed(ABC):

    @abstractmethod
    def attributes(self):
        pass

    @abstractmethod
    def type(self):
        pass
