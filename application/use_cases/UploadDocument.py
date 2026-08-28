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
        pass