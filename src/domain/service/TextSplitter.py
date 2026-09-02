class TextSplitter:
    def __init__(self):
        pass

    @staticmethod
    def split_text(
        text: str,
        chunk_size: int = 512,
        chunk_overlap: int = 64,
    ) -> list[str]:
        chunks = []

        # Prevents hard boundaries; each chunk shares
        # a degree of context with its preceding chunk
        step = chunk_size - chunk_overlap

        if step <= 0:
            raise ValueError("Chunk size must be greater than chunk overlap.")

        for i in range(0, len(text), step):
            chunks.append(text[i:i+chunk_size])

        return chunks