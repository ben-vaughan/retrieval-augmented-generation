from pathlib import Path

from src.application.use_case.UploadPDFService import UploadPDFUseCase
from src.application.use_case.UploadTextService import UploadTextUseCase

from src.domain.exception.FileTypeNotSupportedError import FileTypeNotSupportedError


class Terminal:
    def __init__(
        self,
        upload_text_use_case: UploadTextUseCase,
        upload_pdf_use_case: UploadPDFUseCase,
    ):
        self._upload_text_use_case = upload_text_use_case
        self._upload_pdf_use_case = upload_pdf_use_case

    def run(self) -> None:
        while True:
            self._display_menu()
            choice = input("\nSelect an option (1-3): ").strip()

            match choice:
                case "1":
                    self._handle_upload()
                case "2":
                    self._handle_query()
                case "3":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option. Please try again.")

    def _display_menu(self) -> None:
        print("\n=== RAG Application Menu ===")
        print("1. Upload Document")
        print("2. Ask a Question")
        print("3. Exit")

    def _handle_upload(self) -> None:
        raw_file_path = input("Enter PDF path: ").strip()
        file_path = Path(raw_file_path)

        if not file_path.exists():
            print("Error: File not found.")
            return

        file_type = file_path.suffix.lower()

        try:
            match file_type:
                case '.txt':
                    self._upload_text_use_case.execute(file_path)
                case '.pdf':
                    self._upload_pdf_use_case.execute(file_path)
                case _:
                    raise FileTypeNotSupportedError(file_path)

        except Exception as e:
            print(f"Upload failed: {e}")

    def _handle_query(self) -> None:
        question = input("Enter your question: ").strip()
        if not question:
            return

        try:
            raise NotImplementedError()
        except Exception as e:
            print(f"Query failed: {e}")