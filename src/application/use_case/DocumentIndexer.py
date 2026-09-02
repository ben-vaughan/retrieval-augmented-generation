from pathlib import Path

from src.domain.model.TextChunk import TextChunk

from src.domain.service.TextSplitter import TextSplitter

from src.application.ports.out.EmbeddingModel import EmbeddingModelPort
from src.application.ports.out.VectorStore import VectorStorePort


class DocumentIndexer:
    def __init__(
        self,
        embedding_model: EmbeddingModelPort,
        vector_store: VectorStorePort,
    ):
        self._embedding_model = embedding_model
        self._vector_store = vector_store

    def index_text(self, file_path: Path, text: str):
        text_chunks = TextSplitter.split_text(text)
        text_embeddings = self._embedding_model.embed_text_chunks(text_chunks)

        document_id = file_path.name
        chunks_to_store = []

        for i, (text, embedding) in enumerate(zip(text_chunks, text_embeddings)):
            chunk = TextChunk(
                f"{document_id}_{i}",
                text,
                embedding,
            )
            chunks_to_store.append(chunk)

        self._vector_store.store(chunks_to_store)