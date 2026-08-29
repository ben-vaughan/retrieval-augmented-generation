from src.domain.entities.TextChunk import TextChunk
from src.domain.services.TextSplitter import TextSplitter

from src.ports.into.UploadDocument import UploadDocumentPort

from src.ports.out.EmbeddingModel import EmbeddingModelPort
from src.ports.out.PDFExtractor import PDFExtractorPort
from src.ports.out.VectorStore import VectorStorePort


class UploadDocumentUseCase(UploadDocumentPort):
    def __init__(
        self,
        pdf_extractor: PDFExtractorPort,
        embedding_model: EmbeddingModelPort,
        vector_store: VectorStorePort,
    ):
        self._pdf_extractor = pdf_extractor
        self._embedding_model = embedding_model
        self._vector_store = vector_store

    def execute(self, pdf_path: str):
        extracted_text = self._pdf_extractor.extract_text(pdf_path)

        text_chunks = TextSplitter.split_text(extracted_text)
        text_embeddings = self._embedding_model.embed_text_chunks(text_chunks)

        chunks_to_store = []

        for i, (text, embedding) in enumerate(zip(text_chunks, text_embeddings)):
            chunk = TextChunk(
                f"{pdf_path}_{i}",
                text,
                embedding,
            )
            chunks_to_store.append(chunk)

        self._vector_store.store(chunks_to_store)