from dataclasses import dataclass

@dataclass(frozen=True)
class VectorSearchResult:
    document_id: str
    chunk_text: str
    score: float