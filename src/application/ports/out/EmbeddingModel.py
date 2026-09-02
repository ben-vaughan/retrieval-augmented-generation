from abc import ABC, abstractmethod

from src.domain.model.TextChunk import TextChunk


class EmbeddingModelPort(ABC):
    @abstractmethod
    def embed_text_chunks(
        self,
        text_chunks: list[TextChunk]
    ) -> list[list[float]]:
        pass

    @abstractmethod
    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        pass