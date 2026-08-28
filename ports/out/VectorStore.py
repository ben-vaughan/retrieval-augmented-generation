from abc import ABC, abstractmethod

from application.entities.VectorSearchResult import VectorSearchResult


class VectorStorePort(ABC):
    @abstractmethod
    def store(
        self, 
        document_id: str, 
        chunks: list[str], 
        vectors: list[list[float]],
    ) -> None:
        pass

    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        top_k: int = 3,
    ) -> list[VectorSearchResult]:
        pass

    def delete(
        self,
        document_id: str,
    ) -> None:
        pass

    def flush(
        self,
    ) -> None:
        pass