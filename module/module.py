from abc import ABC, abstractmethod

class AbstractModule(ABC):

    @abstractmethod
    def __init__(self, paramlist):
        pass

    @abstractmethod
    def define_interface(self):
        pass

    def print_wires(self):
        print(f"wires are {self.m_wires}")