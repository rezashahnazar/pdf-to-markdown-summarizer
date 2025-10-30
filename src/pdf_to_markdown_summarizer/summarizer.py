from abc import ABC, abstractmethod
from google import genai
from google.genai.types import HttpOptions
from openai import OpenAI

from pdf_to_markdown_summarizer.config import config


class AIClientBase(ABC):
    @abstractmethod
    def summarize(self, content: str) -> str:
        pass

    def get_full_prompt(self, content: str) -> str:
        return f"""Please provide a compendium of the article in the <ARTICLE> block below and include all important specific details. 
        Answer in markdown format.
        Start with the main Heading of the article and organize the content into sections. Don't include any explanations or other text in your response.
        <ARTICLE>
        {content}
        </ARTICLE>
        """


class GeminiAIClient(AIClientBase):
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        self.base_url = config.GEMINI_BASE_URL
        self.client = genai.Client(
            api_key=self.api_key,
            http_options=HttpOptions(base_url=self.base_url, api_version="v1beta"),
        )
        self.model = "gemini-2.5-flash"

    def summarize(self, content: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    genai.types.Part.from_bytes(
                        data=self.get_full_prompt(content).encode("utf-8"),
                        mime_type="text/plain",
                    ),
                ],
            )
            return response.text
        except Exception as e:
            print(f"Error summarizing content: {e}")
            raise e


class OpenAIClient(AIClientBase):
    def __init__(self):
        self.api_key = config.OPENAI_API_KEY
        self.base_url = config.OPENAI_BASE_URL
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.model = "gpt-4.1-mini"

    def summarize(self, content: str) -> str:
        try:
            response = self.client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "user",
                        "content": self.get_full_prompt(content),
                    },
                ],
            )
            return response.output_text
        except Exception as e:
            print(f"Error summarizing content: {e}")
            raise e


def get_summarizer(ai: str) -> AIClientBase:
    if ai == "openai":
        return OpenAIClient()
    elif ai == "gemini":
        return GeminiAIClient()
    else:
        raise ValueError(f"Invalid AI summarizer client: {ai}")
