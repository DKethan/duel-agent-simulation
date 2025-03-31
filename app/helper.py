import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llama(prompt: str) -> str:
    """
    Send a prompt to the GPT-4 model and return the response.
    Args:
        prompt (str): The input prompt to send to the GPT-4 model.
    Returns:
        str: The response from the GPT-4 model.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
    )

    return response.choices[0].message["content"]