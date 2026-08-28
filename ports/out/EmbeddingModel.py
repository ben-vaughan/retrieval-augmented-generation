from abc import ABC, abstractmethod

class EmbeddingModelPort(ABC):
    @abstractmethod
    def embed_documents(
        self,
        chunks: list[str]
    ) -> list[list[float]]:
        pass

    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        pass