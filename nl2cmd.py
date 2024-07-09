from openai import OpenAI
import sys
import os
from dotenv import load_dotenv

# Function to get the OpenAI API key from environment variables
def get_openai_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    # assign to a global variable!!
    return api_key

# get command line from GPT-3 from prompt
# davinci: completion model: single round
# gpt-3.5-turbo: chat model
def get_command(client, prompt):
    #response = openai.Completion.create( # single turn: text completion models only
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # engine
        messages=[
            {"role": "system", "content": """
            You are a helpful chat assistant that answers questions from users using a terminal on a Linux computer.  
            """},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=0,
        max_tokens=100,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0,
    )

   # command = response.choices[0].text.strip()
    command = response.choices[0].message.content.strip()
    return command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nl2cmd.py <natural_language_description>")
        sys.exit(1)

    #prompt = sys.argv[1]
    prompt = ' '.join(sys.argv[1:])
    
    #prompt =f"Translate the following English description to a Linux command: {prompt}"
    
    client = OpenAI(api_key=get_openai_api_key())
    response = get_command(client, prompt)
    #print(f"Suggested command: {response}")
    print(f"{response}")

