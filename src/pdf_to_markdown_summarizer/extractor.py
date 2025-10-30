from pypdf import PdfReader


class PDFExtractor:
    def extract(self, path_to_input_file: str) -> str:
        try:
            reader = PdfReader(path_to_input_file)
            pages = reader.pages
            full_content = ""
            for page in pages:
                full_content += page.extract_text()
            return full_content
        except Exception as e:
            print(f"Error extracting content from {path_to_input_file}: {e}")
            raise e


def get_extractor() -> PDFExtractor:
    return PDFExtractor()
