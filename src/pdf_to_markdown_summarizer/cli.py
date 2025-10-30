import argparse

from pdf_to_markdown_summarizer.extractor import get_extractor
from pdf_to_markdown_summarizer.summarizer import get_summarizer
from pdf_to_markdown_summarizer.utils import save_content_to_markdown_file


def main():
    parser = argparse.ArgumentParser(
        description="Summarize PDF files into markdown format using AI"
    )
    parser.add_argument("--file", type=str, required=True, help="Path to PDF file")
    parser.add_argument(
        "--output",
        type=str,
        required=False,
        default="output",
        help="Output directory for markdown files",
    )
    parser.add_argument(
        "--ai",
        type=str,
        required=False,
        default="openai",
        choices=["openai", "gemini"],
        help="AI provider to use (default: openai)",
    )
    args = parser.parse_args()

    summarizer = get_summarizer(args.ai)
    extractor = get_extractor()

    extracted_content = extractor.extract(args.file)
    summarized_content = summarizer.summarize(extracted_content)
    save_content_to_markdown_file(summarized_content, args.file, args.output)


if __name__ == "__main__":
    main()
