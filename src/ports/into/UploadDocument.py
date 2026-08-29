from abc import ABC, abstractmethod


class UploadDocumentPort(ABC):
    @abstractmethod
    def execute(self, pdf_path: str):
        pass