from abc import ABC, abstractmethod

from application.entities import UserQuery


class UserQueryPort(ABC):
    @abstractmethod
    def ask(self, query: UserQuery):
        """
        Processes a user question through the RAG pipeline and returns the answer.
        """
        pass