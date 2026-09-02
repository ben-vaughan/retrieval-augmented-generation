from abc import ABC, abstractmethod


class PDFExtractorPort(ABC):
    @abstractmethod
    def extract_text(
        self,
        path: str,
    ) -> str:
        pass