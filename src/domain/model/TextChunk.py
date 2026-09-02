class TextChunk:
    def __init__(
        self,
        id: str,
        text: str,
        embedding: list[float]
    ):
        self.id = id
        self.text = text
        self.embedding = embedding