from pathlib import Path

from src.application.ports.into.IndexDocument import IndexDocumentPort
from src.application.ports.into.UploadDocument import UploadDocumentPort


class UploadTextUseCase(UploadDocumentPort):
    def __init__(
        self,
        document_indexer: IndexDocumentPort,
    ):
        self._document_indexer = document_indexer

    def execute(self, path: Path):
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        self._document_indexer.index_text(
            path,
            text
        )