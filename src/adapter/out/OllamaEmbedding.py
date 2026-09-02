import requests

from src.domain.model.TextChunk import TextChunk

from application.ports.out.EmbeddingModel import EmbeddingModelPort


class OllamaEmbeddingAdapter(EmbeddingModelPort):
    def __init__(self):
        self._model_name = "nomic-embed-text"
        self._model_host = "http://localhost:11434/api/embeddings"

    def embed_text_chunks(
        self, 
        text_chunks: list[TextChunk]
    ):
        embeddings = []
        for text_chunk in text_chunks:
            response = requests.post(
                self._model_host,
                json = {
                    "model": self._model_name,
                    "prompt": text_chunk,
                }
            )
            response.raise_for_status()
            embeddings.append(response.json()["embedding"])

        return embeddings

    def embed_query(
        self,
        query: str
    ):
        pass