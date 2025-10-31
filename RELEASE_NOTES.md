# Release Notes

## v0.1.0 (Initial Release)

### Features
- Extract text from PDF files using pypdf
- Generate AI-powered markdown summaries using OpenAI or Google Gemini
- Command-line interface (`pdf-to-markdown` command)
- Python API for programmatic usage
- Flexible configuration via environment variables or `.env` file
- Support for both OpenAI and Google Gemini APIs

### Installation
```bash
pip install pdf-to-markdown-summarizer
```

### Usage
```bash
pdf-to-markdown --file document.pdf --ai openai
```

### Requirements
- Python >= 3.12
- OpenAI API key (if using OpenAI) or Google Gemini API key (if using Gemini)

