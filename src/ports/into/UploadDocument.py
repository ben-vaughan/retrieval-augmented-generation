from abc import ABC, abstractmethod


class UploadDocumentPort(ABC):
    @abstractmethod
    def execute(self, path: str):
        pass