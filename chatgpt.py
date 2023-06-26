# chatgpt.py

import openai

# Set the ChatGPT access token (adjust it based on your actual situation)
openai.api_key = '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'

def generate_response(user_input: object) -> object:
    # Generate a reply using ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated reply
    reply = response.choices[0].text.strip()

    # Return the generated reply
    return reply
