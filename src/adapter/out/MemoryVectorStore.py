import heapq
from typing import Dict, List

from domain.service.VectorOperator import VectorOperator
from src.domain.model.TextChunk import TextChunk
from src.domain.model.VectorSearchResult import VectorSearchResult
from src.application.ports.out.VectorStore import VectorStorePort


class MemoryVectorStoreAdapter(VectorStorePort):
    def __init__(self):
        self._chunks: Dict[str, TextChunk] = {}

    def add(
        self, 
        chunks: list[TextChunk]
    ) -> None:
        for chunk in chunks:
            self._chunks[chunk.id] = chunk

    def search(
        self,
        query_vector: List[float],
        top_k: int = 3,
    ) -> List[VectorSearchResult]:
        matches = []

        for _, chunk in self._chunks.items():
            score = VectorOperator.cosine_similarity(
                query_vector,
                chunk.embedding
            )

            if len(matches) < top_k:
                heapq.heappush(matches, (score, chunk))
            elif score > matches[0][0]:
                heapq.heapreplace(matches, (score, chunk))

        matches.sort(key=lambda item: item[0], reverse=True)
        return [
            VectorSearchResult(chunk=chunk, score=score)
            for score, chunk in matches
        ]

    def delete(
        self,
        id: str,
    ) -> None:
        del self._store[id]

    def flush(
        self,
    ) -> None:
        self._store.clear()