from abc import ABC, abstractmethod


class QueryDocumentPort(ABC):
    @abstractmethod
    def execute(self, query: str):
        pass