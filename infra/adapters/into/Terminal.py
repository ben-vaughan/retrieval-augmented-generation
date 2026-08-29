from pathlib import Path

from src.ports.into.UploadDocument import UploadDocumentPort


class Terminal:
    def __init__(
        self,
        upload_use_case: UploadDocumentPort,
        query_use_case: QueryDocumentPort,
    ):
        self._upload_use_case = upload_use_case
        self._query_use_case = query_use_case

    def run(self) -> None:
        while True:
            self._display_menu()
            choice = input("\nSelect an option (1-5): ").strip()

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
        file_path = input("Enter PDF path: ").strip()
        if not Path(file_path).exists():
            print("Error: File not found.")
            return

        try:
            self._upload_use_case(file_path)
            print("Document processed successfully.")
        except Exception as e:
            print(f"Upload failed: {e}")

    def _handle_query(self) -> None:
        question = input("Enter your question: ").strip()
        if not question:
            return

        try:
            answer = self._query_use_case.execute(question)
            print(f"\n--- Answer --- \n{answer}")
        except Exception as e:
            print(f"Query failed: {e}")