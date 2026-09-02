from src.domain.services.DocumentIndexer import DocumentIndexer

from src.application.use_cases.UploadPDF import UploadPDFUseCase
from src.application.use_cases.UploadText import UploadTextUseCase

from infra.adapters.into.Terminal import Terminal

from infra.adapters.out.PyMuPDF import PyMuPDFAdapter
from infra.adapters.out.OllamaEmbedding import OllamaEmbeddingAdapter
from infra.adapters.out.MemoryVectorStore import MemoryVectorStoreAdapter


if __name__ == '__main__':
    pdf_extractor = PyMuPDFAdapter()
    embedding_model = OllamaEmbeddingAdapter()
    vector_store = MemoryVectorStoreAdapter()

    document_indexer = DocumentIndexer(
        embedding_model,
        vector_store
    )

    upload_text_use_case = UploadTextUseCase(document_indexer)
    upload_pdf_use_case = UploadPDFUseCase(
        pdf_extractor,
        document_indexer
    )

    terminal = Terminal(
        upload_pdf_use_case=upload_pdf_use_case,
        upload_text_use_case=upload_text_use_case
    )
    terminal.run()
