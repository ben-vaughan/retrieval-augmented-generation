from src.application.use_case.UploadPDFService import UploadPDFUseCase
from src.application.use_case.UploadTextService import UploadTextUseCase
from src.application.use_case.IndexTextService import IndexTextService

from src.adapter.into.Terminal import Terminal

from src.adapter.out.PyMuPDF import PyMuPDFAdapter
from src.adapter.out.OllamaEmbedding import OllamaEmbeddingAdapter
from src.adapter.out.MemoryVectorStore import MemoryVectorStoreAdapter


if __name__ == '__main__':
    pdf_extractor = PyMuPDFAdapter()
    embedding_model = OllamaEmbeddingAdapter()
    vector_store = MemoryVectorStoreAdapter()

    document_indexer = IndexTextService(
        embedding_model,
        vector_store
    )

    upload_text_use_case = UploadTextUseCase(
        document_indexer
    )
    upload_pdf_use_case = UploadPDFUseCase(
        pdf_extractor,
        document_indexer
    )

    terminal = Terminal(
        upload_pdf_use_case=upload_pdf_use_case,
        upload_text_use_case=upload_text_use_case
    )
    terminal.run()
