import pymupdf
from pathlib import Path

from src.ports.out.PDFExtractor import PDFExtractorPort


class PyMuPDF(PDFExtractorPort):
    def __init__(
        self
    ):
        self._BASE_DIR = Path(__file__).resolve().parent.parent
        self._TEMP_DIR = self._BASE_DIR / "tmp"

    def extract_text(
            self, 
            path: str
        ):
        document = pymupdf.open(path)

        OUTPUT_PATH = self._TEMP_DIR / "pdf_output.txt"

        out = open(OUTPUT_PATH, "wb")
        for page in document:
            text = page.get_text().encode("utf8")
            out.write(text)

        out.close()