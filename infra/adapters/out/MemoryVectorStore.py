from src.domain.entities.TextChunk import TextChunk
from src.domain.entities.VectorSearchResult import VectorSearchResult
from src.ports.out.VectorStore import VectorStorePort


class MemoryVectorStoreAdapter(VectorStorePort):
    def __init__(self):
        pass

    def store(
        self, 
        chunks: list[TextChunk]
    ) -> None:
        pass

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