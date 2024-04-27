import os
import openai


OPENAI_APIKEY = os.environ["OPENAI_APIKEY"]


def get_response(prompt, temperature: int = 0):
    client = openai.OpenAI(
        api_key=OPENAI_APIKEY,
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=temperature,
        max_tokens=1024,
    )

    text_response = response.choices[0].message.content

    return text_response
