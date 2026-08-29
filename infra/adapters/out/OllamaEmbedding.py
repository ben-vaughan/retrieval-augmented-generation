from src.domain.entities.TextChunk import TextChunk
from src.ports.out.EmbeddingModel import EmbeddingModelPort


class OllamaEmbeddingAdapter(EmbeddingModelPort):
    def embed_text_chunks(
        self, 
        text_chunks: list[TextChunk]
    ):
        pass