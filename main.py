from adapters.into.UploadDocument import UploadDocumentUseCase
from infra.adapters.out.PyMuPDF import PyMuPDFAdapter


def main():
    pdf_extractor = PyMuPDFAdapter()
    embedding_model = OllamaEmbeddingAdapter() 

    upload_use_case = UploadDocumentUseCase(
        pdf_extractor,
        embedding_model,
        vector_store
    )

    file_path = input("Enter file path")
    upload_use_case.execute(file_path)