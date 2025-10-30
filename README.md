# PDF To Markdown Summarizer

A Python package that extracts text from PDF files and generates comprehensive markdown summaries using AI-powered language models. Supports both OpenAI and Google Gemini APIs, allowing you to transform PDF documents into well-structured markdown compendiums with all important details preserved.

## Features

- Extract text from PDF files
- Generate AI-powered markdown summaries using OpenAI or Google Gemini
- Flexible configuration via environment variables or `.env` file
- Simple command-line interface
- Python API for programmatic usage
- Preserves important details and structure from source documents

## Installation

```bash
pip install pdf-to-markdown-summarizer
```

## Quick Start

1. **Install the package:**
   ```bash
   pip install pdf-to-markdown-summarizer
   ```

2. **Set up your API key** (choose one provider):
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```
   Or for Gemini:
   ```bash
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```

3. **Run the command:**
   ```bash
   pdf-to-markdown --file document.pdf --ai openai
   ```

## Configuration

**Important**: You only need to configure API keys for the AI providers you plan to use. If you only want to use OpenAI, you can skip setting `GEMINI_API_KEY`. Similarly, if you only want to use Gemini, you can skip setting `OPENAI_API_KEY`.

### Option 1: Environment Variables (Recommended)

Set the environment variables in your shell for the provider(s) you want to use:

**If using OpenAI only:**
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

**If using Gemini only:**
```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

**If using both providers:**
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
export GEMINI_API_KEY="your_gemini_api_key_here"
```

**Optional**: You can also customize the base URLs (defaults work for most cases):
```bash
export OPENAI_BASE_URL="https://api.openai.com/v1"  # Optional
export GEMINI_BASE_URL="https://generativelanguage.googleapis.com"  # Optional
```

### Option 2: .env File

Create a `.env` file in your current working directory with only the keys you need:

**If using OpenAI only:**
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

**If using Gemini only:**
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

**If using both providers:**
```bash
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

You can use the `.env.example` file in the repository as a template. The package will automatically detect and load the `.env` file if it exists. Environment variables take precedence over `.env` file values.

## Usage

### Command Line Interface

The `pdf-to-markdown` command provides a simple way to process PDF files:

```bash
pdf-to-markdown --file path/to/document.pdf --output output_directory --ai openai
```

#### Arguments

- `--file` (required): Path to the PDF file you want to process
- `--output` (optional): Output directory for markdown files (defaults to `"output"`)
- `--ai` (optional): AI provider to use - `openai` or `gemini` (defaults to `"openai"`)

#### Examples

Process a PDF with OpenAI:
```bash
pdf-to-markdown --file research_paper.pdf --ai openai
```

Process a PDF with Gemini and specify custom output directory:
```bash
pdf-to-markdown --file document.pdf --output summaries --ai gemini
```

Process with default settings (OpenAI, output to `output/` directory):
```bash
pdf-to-markdown --file document.pdf
```

### Python API

You can also use the package programmatically in your Python code:

```python
from pdf_to_markdown_summarizer import (
    get_summarizer,
    get_extractor,
    save_content_to_markdown_file
)

summarizer = get_summarizer("openai")
extractor = get_extractor()

extracted_content = extractor.extract("document.pdf")
summarized_content = summarizer.summarize(extracted_content)
save_content_to_markdown_file(
    summarized_content,
    "document.pdf",
    "output"
)
```

#### Available Functions

- `get_summarizer(ai: str) -> AIClientBase`: Get an AI summarizer instance (`"openai"` or `"gemini"`)
- `get_extractor() -> PDFExtractor`: Get a PDF text extractor instance
- `save_content_to_markdown_file(content: str, input_file: str, output_dir: str) -> str`: Save summarized content to a markdown file

#### Advanced Usage

You can also import specific classes for more control:

```python
from pdf_to_markdown_summarizer import (
    PDFExtractor,
    OpenAIClient,
    GeminiAIClient
)

extractor = PDFExtractor()
content = extractor.extract("document.pdf")

openai_client = OpenAIClient()
summary = openai_client.summarize(content)
```

## Requirements

- Python >= 3.12
- **At least one** of the following API keys:
  - OpenAI API key (required only if using `--ai openai`)
  - Google Gemini API key (required only if using `--ai gemini`)

## Dependencies

- `google-genai>=1.47.0` - Google Gemini API client
- `openai>=2.6.1` - OpenAI API client
- `pydantic-settings>=2.11.0` - Configuration management
- `pypdf[full]>=6.1.3` - PDF text extraction
- `python-dotenv>=1.2.1` - Environment variable loading

## How It Works

1. **Extraction**: The package extracts all text content from the PDF file using `pypdf`
2. **Summarization**: The extracted text is sent to your chosen AI provider (OpenAI or Gemini) with a prompt to create a comprehensive markdown compendium
3. **Output**: The AI-generated markdown summary is saved to a file in your specified output directory

The AI is instructed to:
- Include all important specific details
- Organize content into sections with proper headings
- Format everything in markdown
- Start with the main heading of the article

## License

MIT License

Copyright (c) 2025 Reza Shahnazar

## Author

**Reza Shahnazar**

- GitHub: [@rezashahnazar](https://github.com/rezashahnazar)
- Email: reza.shahnazar@gmail.com

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or feature requests, please open an issue on the [GitHub repository](https://github.com/rezashahnazar/pdf-to-markdown-summarizer/issues).
