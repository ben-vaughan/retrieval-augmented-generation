class FileTypeNotSupportedError(Exception):
    """Raised when an uploaded file format is not supported."""
    def __init__(self, extension: str):
        super().__init__(f"Unsupported file format '{extension}'. Only .pdf and .txt are supported.")