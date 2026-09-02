from domain.services.DocumentIndexer import DocumentIndexer
from ports.into.UploadDocument import UploadDocumentPort
from ports.out.EmbeddingModel import EmbeddingModelPort
from ports.out.VectorStore import VectorStorePort


class UploadTextUseCase(UploadDocumentPort):
    def __init__(
        self,
        document_indexer: DocumentIndexer
    ):
        self._document_indexer = document_indexer

    def execute(self, path: str):
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        self._document_indexer.index_text(
            path,
            text
        )