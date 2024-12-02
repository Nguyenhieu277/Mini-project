import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("GITHUB_TOKEN")
        self.endpoint = "https://models.inference.ai.azure.com"
        self.model_name = "gpt-4o-mini"
        try:
            self.client = OpenAI(
                base_url=self.endpoint,
                api_key=self.token,
            )
        except OpenAIError as e:
            print(f"Failed to initialize OpenAI client: {e}")
            self.client = None

    def get_response(self, messages, temperature=1.0, top_p=1.0, max_tokens=1000):
        if not self.client:
            return "OpenAI client is not initialized."
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_tokens,
                model=self.model_name
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            return f"Failed to get response from OpenAI: {e}"

# if __name__ == "__main__":
#     client = OpenAIClient()
#     messages = [
#         {
#             "role": "system",
#             "content": "You are a helpful assistant to recommend anime",
#         },
#         {
#             "role": "user",
#             "content": "I want to romance anime ",
#         }
#     ]
#     response = client.get_response(messages)
#     print(response)