from pathlib import Path

from src.application.use_case.DocumentIndexer import DocumentIndexer

from src.application.ports.into.UploadDocument import UploadDocumentPort

from src.application.ports.out.PDFExtractor import PDFExtractorPort


class UploadPDFUseCase(UploadDocumentPort):
    def __init__(
        self,
        pdf_extractor: PDFExtractorPort,
        document_indexer: DocumentIndexer,
    ):
        self._pdf_extractor = pdf_extractor
        self._document_indexer = document_indexer

    def execute(self, path: Path):
        text = self._pdf_extractor.extract_text(path)

        self._document_indexer.index_text(
            path,
            text
        )