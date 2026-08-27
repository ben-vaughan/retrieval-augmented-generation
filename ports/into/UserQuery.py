from abc import ABC, abstractmethod

from model import UserQuery


class UserQueryPort(ABC):
    @abstractmethod
    def ask(self, query: UserQuery):
        """
        Processes a user question through the RAG pipeline and returns the answer.
        """
        raise NotImplementedError()