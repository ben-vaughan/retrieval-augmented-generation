from application.entities.Chunk import Chunk
from application.services.TextSplitter import TextSplitter

from ports.out.EmbeddingModel import EmbeddingModelPort
from ports.out.PDFExtractor import PDFExtractorPort
from ports.out.VectorStore import VectorStorePort


class UploadDocumentUseCase:
    def __init__(
        self,
        pdf_extractor: PDFExtractorPort,
        embedding_model: EmbeddingModelPort,
        vector_store: VectorStorePort,
    ):
        self._pdf_extractor = pdf_extractor
        self._embedding_model = embedding_model
        self._vector_store = vector_store

    def upload(self, pdf_path: str):
        extracted_text = self._pdf_extractor.extract_text(pdf_path)

        text_chunks = TextSplitter.split_text(extracted_text)
        text_embeddings = self._embedding_model.embed_text_chunks(text_chunks)

        chunks_to_store = []

        for i, (text, embedding) in enumerate(zip(text_chunks, text_embeddings)):
            chunk = Chunk(
                f"{pdf_path}_{i}",
                text,
                embedding,
            )
            chunks_to_store.append(chunk)

        self._vector_store.store(chunks_to_store)