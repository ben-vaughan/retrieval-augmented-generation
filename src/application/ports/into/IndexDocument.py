from abc import ABC, abstractmethod
from pathlib import Path


class IndexDocumentPort(ABC):
    @abstractmethod
    def execute(
        self, 
        file_path: Path, 
        text: str
    ):
        pass