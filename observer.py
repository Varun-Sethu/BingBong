from __future__ import annotations
from abc import ABC, abstractmethod



# Observer subject that is to be tracked
class Observer_Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass



class Observer(ABC):
    @abstractmethod
    def update(self, subject: Observer_Subject):
        pass