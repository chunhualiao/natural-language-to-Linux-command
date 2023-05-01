import openai
import sys
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from the .env file

# Replace with your own API key
openai.api_key = os.getenv("OPENAI_API_KEY") #"your-api-key"

# get command line from GPT-3 from prompt
# davinci: completion model: single round
# gpt-3.5-turbo: chat model
def get_command(prompt):
    #response = openai.Completion.create( # single turn: text completion models only
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # engine
        messages=[
            {"role": "system", "content": """
            You are a helpful chat assistant that answers questions from users using a terminal on a Linux computer.  
            """},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=0.5,
        max_tokens=200,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0,
    )

   # command = response.choices[0].text.strip()
    command = response['choices'][0]['message']['content'].strip()
    return command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nl2cmd.py <natural_language_description>")
        sys.exit(1)

    #prompt = sys.argv[1]
    prompt = ' '.join(sys.argv[1:])
    
    #prompt =f"Translate the following English description to a Linux command: {prompt}"
    
    response = get_command(prompt)
    #print(f"Suggested command: {response}")
    print(f"{response}")

